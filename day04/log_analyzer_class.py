import json

class LogAnalyzer:

    #get the log file

    def __init__(self,logfile,output_file):

        self.filename= logfile
        self.output_file = output_file
    
    #read the log file

    def read_log(self):
        with open(self.filename,"r") as file:
            return file.readlines()
        

    def write_json(self,log_count):
        with open(self.output_file,"w+") as file:
            json.dump(log_count,file)
    
    def analyze(self):
        log_count = {
            "INFO" : 0,
            "WARNING" : 0,
            "ERROR" : 0,
        }

        lines = self.read_log()

        for line in lines:
            if "INFO" in line:
                log_count.update({"INFO": log_count["INFO"]+1})
            elif "WARNING" in line:
                log_count.update({"WARNING": log_count["WARNING"]+1})
            elif "ERROR" in line:
                log_count.update({"ERROR": log_count["ERROR"]+1})
            else:
                pass
        
        self.write_json(log_count)
    
log1_count = LogAnalyzer("app.log","output.json")

content = log1_count.analyze()

log2_count =  LogAnalyzer("app2.log","output2.json")

content1 = log2_count.analyze()