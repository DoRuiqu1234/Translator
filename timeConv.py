from datetime import datetime
import pytz

class myTimeConverter:
    def __init__(self) -> None:
        self.inputFormat = "%m/%d/%Y %I:%M %p"
        self.example = "07/17/2017 6:12 AM"

        self.outputFormat = "%x %I:%M %p, %A"
        self.timezones = ['Asia/Calcutta', 'America/New_York', 'America/Santiago']
        self.timezones_shortNames = ['India', 'New York', 'Chile']

    def get_time(self, when=-1) -> dict:
        returningProduct = {}
        if when == -1:
            utcmoment_naive = datetime.utcnow()
            when = utcmoment_naive.replace(tzinfo=pytz.utc)
        for i in range(0, len(self.timezones)):
            localDatetime = when.astimezone(pytz.timezone(self.timezones[i]))
            returningProduct[self.timezones_shortNames[i]] = localDatetime.strftime(self.outputFormat)
        return returningProduct

    def dictToSimple(self, target) -> str:
        returningProduct = ''
        items = list(target.items())
        for i in range(0, len(items)):
            item = items[i]
            returningProduct +=  f'[{self.timezones_shortNames[i]}]:\t{item[1]}\n'
        return returningProduct
    
    def get(self, when=-1) -> str:
        if when == -1:
            return f'Times in different locations: \n{self.dictToSimple(self.get_time(when))}'
        
        try:
            when = datetime.strptime(when, self.inputFormat).replace(tzinfo=pytz.utc)
        except:
            return f'Please write the time in form of {self.inputFormat}.\nOne example is: {self.example}.'
        
        return f'Times in different locations: \n{self.dictToSimple(self.get_time(when))}'
