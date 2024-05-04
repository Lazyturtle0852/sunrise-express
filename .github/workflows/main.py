from urllib import request
from bs4 import BeautifulSoup
import re
import datetime
from datetime import date, timedelta
print("【寝台特急サンライズ号ノビノビ座席　1ヶ月後までの空席状況をご案内します】")
date = datetime.datetime.now()
from pipedream.script_helpers import (steps, export)
export('時刻', str(datetime.datetime.today())) # 2017-11-08 23:58:55.230456
month = str(date.month)
day = str(date.day)


one_month_one_day_from_today = date + timedelta(days=31)

while int(day) <= 31 and int(month) <= 12:
  if len(day) == 1:
    day = "0" + day
  if len(month) == 1:
    month = "0" + month
  date = "2024" + month + day
  print(date)
  url = 'https://e5489.jr-odekake.net/e5489/cspc/CBDayTimeArriveSelRsvMyDiaPC?inputDepartStName=%93%8C%8B%9E&inputArriveStName=%89%AA%8ER&inputType=0&inputDate='+date+'&inputHour=21&inputMinute=00&inputUniqueDepartSt=1&inputUniqueArriveSt=1&inputSearchType=2&inputTransferDepartStName1=%93%8C%8B%9E&inputTransferArriveStName1=%89%AA%8ER&inputTransferDepartStUnique1=1&inputTransferArriveStUnique1=1&inputTransferTrainType1=0001&inputSpecificTrainType1=2&inputSpecificBriefTrainKana1=%BB%BE%C4%20%20000&SequenceType=0&inputReturnUrl=goyoyaku/campaign/sunriseseto_izumo/form.html&RTURL=https://www.jr-odekake.net/goyoyaku/campaign/sunriseseto_izumo/form.html&'
  response = request.urlopen(url)
  soup = BeautifulSoup(response, 'html.parser')
  response.close()
  test1 = soup.select_one('body > main > section:nth-child(3) > section:nth-child(4) > form > div > section:nth-child(1) > div.route-train-list__section-body > div.route-train-list__seat-info.js-filfac-scope > table > tbody > tr > td:nth-child(1) > label > span > span > img')
  if test1 is None:
    print("❌")
    from pipedream.script_helpers import (steps, export)
    export(date, '❌')
  else:
    print("⭕️")
    from pipedream.script_helpers import (steps, export)
    export(date, '⭕️')
  print(url)
  print(" ")
  day = str(int(day) + 1)
  if int(day) == 32:
    month = str(int(month) + 1)
    day = "01"
    if int(month) == 13:
      month = "01"
      year = str(int(year) + 1)
  if date == one_month_one_day_from_today.strftime("%Y%m%d"):
    break


#「この経路は選択できません」分岐にした方がよさそう。

