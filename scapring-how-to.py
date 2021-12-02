
#writing to file
with open(f"file_name{file_no+1}.csv",'w', encoding='utf-8_sig',newline='') as csvfile: #using utf-8_sig instead of utf-8 for valid encodding of special chars
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['col1','..col'])
    for row in rows:
        csvwriter.writerow(row)
        
