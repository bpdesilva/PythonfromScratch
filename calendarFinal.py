import calendar #import calendar module

calen =calendar.TextCalendar(calendar.SUNDAY)#create caledar in text format
st = calen.formatmonth(2018,6,0,0)#define a month and format
print(st)#print calendar

htmlCalen =calendar.HTMLCalendar(calendar.SUNDAY)#createcalendar in html format
htmSt = htmlCalen.formatmonth(2018,1)#define a month and format
print(htmSt)#print html table

for x in calen.itermonthdays(2018,3):
    print(x)

for mn in calendar.month_name:#iterate through the months
    print(mn)#print months

for dn in calendar.day_name:#iterate through the days
    print(dn)#print the names of the days

#Case: Study : print out the SUNDAY's of the year to have Meetings
for mon in range(1,13):#iterate through the months
    someVal =calendar.monthcalendar(2018,mon)#defining year and months
    firstWeek = someVal[0] #setting up an array with the SUNDAY's on the first Week
    secondWeek = someVal[1] #setting up an array with the SUNDAY's on the second Week
    if firstWeek[calendar.SUNDAY]!=0:#if not in this month
        Meeting = firstWeek[calendar.SUNDAY]
    else:#if in next month
        Meeting= secondWeek[calendar.SUNDAY]
        print("%10s %4d" (calendar.month_name[mon], Meeting))#print the
