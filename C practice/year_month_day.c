//Ex 5-8, 5-9
#include <stdio.h>

static char day1[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
static char day2[] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
static char* daytab[] = {day1, day2};

/* day_of_year: set day of year from month & day */
int day_of_year(int year, int month, int day) {
    int i, leap;
    if (month<1 || month>12){
        printf("invalid month");
    }
    leap = (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    if (day > daytab[leap][month] || day < 0){
        printf("invalid day");
    }
    for (i = 1; i < month; i++)
        day += *(daytab[leap]+i);
    return day;
}

/* month_day: set month, day from day of year */
void month_day(int year, int yearday, int *pmonth, int *pday) {
    int i, leap;
    leap = (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    if (yearday<0 || yearday>365+leap){printf("invalid yearday");}
    for (i = 1; yearday > *(daytab[leap]+i); i++)
        yearday -= *(daytab[leap]+i);
    *pmonth = i;
    *pday = yearday;
}

int main(){
    int month;
    int day;
    printf("%d\n", day_of_year(2013, 2, 3));
    month_day(2013, 123, &month, &day);
    printf("%d %d\n", month, day);
    return 0;
}
