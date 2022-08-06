import subprocess
import datetime


def get_date():
    today = datetime.date.today()
    today_str = today.strftime('%Y/%m/%d')  # to string
    yesterday = today - datetime.timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')  # to string
    return today_str, yesterday_str


def subprocess_cmd(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    stdout = p.communicate()[0].decode('utf-8').split()
    return stdout


try:
    # date
    today, yesterday = get_date()

    # df
    # get disc size
    df_out = subprocess_cmd("df -h")
    df_str = f"DISC SIZE[USED:{df_out[16]}, SIZE:{df_out[14]} {df_out[17]}]"

    # free
    # get memory size
    free_out = subprocess_cmd("free -m")
    free_str = f"MEMORY[TOTAL:{free_out[7]}, USED:{free_out[8]}, FREE:{free_out[9]}, {float(free_out[8])/float(free_out[7])*100:.2f}%]"

    # vnstat
    # get traffic size
    vnstat_out = subprocess_cmd(f"vnstat -d|grep {yesterday}")

    if vnstat_out:
        # if you can get traffic size
        vnstat_str = f"TRAFFIC[DATE:{vnstat_out[0]}, RECEPTIONS:{vnstat_out[1]}{vnstat_out[2]}, SENDS: {vnstat_out[4]}{vnstat_out[5]}]"
        print(today+"\\n"+df_str + "\\n" + free_str +
              "\\n"+vnstat_str)  # send infomation
    else:
        print(today+"\\n"+df_str + "\\n" +
              free_str+"\\nERR: 昨日のトラフィックデータが取得されませんでした")
except:
    print("@here\\nERR: エラーが発生しています．コードのチェックをお願いします．")
