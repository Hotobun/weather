import matplotlib.pyplot as plt  
import db   

def get_data(date):
    # date type : str
    # rtype : dict
    items = db.query_weather(date)
    max_t = []
    min_t = []
    day = []
    count = 1
    for i in items:
        max_t.append(i.max_t)
        min_t.append(i.min_t)
        day.append("{}".format(count))
        count += 1
    d = {
        "date":date,
        "max_t":max_t,
        "min_t":min_t,
        "day":day,
    }
    return d

def main():
    d = get_data(input("1.输入年份 例: 2012\n2.输入年份+空格+月份 例: 2016 5\n"))
    plt.plot( d['min_t'],'b-')
    plt.plot( d['max_t'],'r-')
    plt.title(d["date"])
    plt.axis([0,len(d['day']),0,max(d['max_t'])+2])
    plt.grid(axis="y")
    plt.show()

if __name__ == "__main__":
    main()