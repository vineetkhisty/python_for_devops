import json

def read_logs():
    with open("app.log","r") as file:
        return file.readlines()

def analyzer(lines):
    log_count ={
        "INFO": 0,
        "Warning": 0,
        "Error": 0
    }

    for line in lines:
        if "INFO" in line:
            log_count.update({"INFO": log_count["INFO"]+1})
        elif "WARNING" in line:
            log_count.update({"Warning": log_count["Warning"]+1})
        elif "ERROR" in line:
            log_count.update({"Error": log_count["Error"]+1})
        else:
            pass
            
    return log_count

def write_json(log_count):
    with open("output.json","w+") as file:
        json.dump(log_count,file)

lines = read_logs()
log_count = analyzer(lines)
write_json(log_count)
