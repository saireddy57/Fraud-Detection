from datetime import datetime,timedelta,time,date

class app_log:

    def log(self,file_obj,log_message):
        self.start_datetime = datetime.now()
        self.date =self.start_datetime.date()
        self.time = self.start_datetime.strftime("%H:%M:%S")
        file_obj.write(
            str(self.date) + "/" + str(self.time) + "\t\t" + log_message +"\n")