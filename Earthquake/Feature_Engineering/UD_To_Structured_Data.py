unstructured_data = """
Origin Time       1996/05/23 18: 36:00
Lat.              38.653
Long.             142.313
Depth. (km)       39
Mag.              5.0
Station Code      IWT003
Station Lat.      40.0083
Station Long.     141.8861
Station Height(m) 9
Record Time       1996/05/23 18: 36:58
Sampling Freq(Hz) 100Hz
Duration Time(s)  59
Dir.              U-D
Scale Factor      2000(gal)/8388608
Max. Acc. (gal)   4.764
Last Correction   1996/05/23 18: 00:00
"""

ud_lines = unstructured_data.split('\n')

Max_Acc = None
Mag_value = None
Origin_Time = None
Lat = None
Long = None
Depth = None
Station_Code = None
Station_Lat = None
Station_Long = None
Station_Height = None
Record_Time = None
Sampling_Freq = None
Duration = None
Dir_value = None
Scale_Factor_Numerator = None
Scale_Factor_Denominator = None
Last_Correction = None

for line in ud_lines:
    if 'Max. Acc. (gal)' in line:
        Max_Acc = float(line.split()[-1])
    elif 'Mag.' in line:
        Mag_value = float(line.split()[-1])
    elif 'Origin Time' in line:
        Origin_Time = line.split('       ')[-1].strip()
    elif 'Lat.' in line:
        Lat = float(line.split()[-1])
    elif 'Long.' in line:
        Long = float(line.split()[-1])
    elif 'Depth. (km)' in line:
        Depth = float(line.split()[-1])
    elif 'Station Code' in line:
        Station_Code = line.split()[-1]
    elif 'Station Lat.' in line:
        Station_Lat = float(line.split()[-1])
    elif 'Station Long.' in line:
        Station_Long = float(line.split()[-1])
    elif 'Station Height(m)' in line:
        Station_Height = float(line.split()[-1])
    elif 'Record Time' in line:
        Record_Time = line.split('       ')[-1].strip()
    elif 'Sampling Freq(Hz)' in line:
        Sampling_Freq = int(line.split()[-1].split('Hz')[0])
    elif 'Duration Time(s)' in line:
        Duration = int(line.split()[-1])
    elif 'Dir.' in line:
        Dir_value = line.split()[-1]
    elif 'Scale Factor' in line:
        Scale_Factor_Numerator = float(line.split()[2].split('(')[0])
        Scale_Factor_Denominator = float(line.split('/')[-1])
    elif 'Last Correction' in line:
        Last_Correction = line.split('       ')[-1].strip()

print("Max_Acc:", Max_Acc)
print("Mag_value:", Mag_value)
print("Origin_Time:", Origin_Time)
print("Lat:", Lat)
print("Long:", Long)
print("Depth:", Depth)
print("Station_Code:", Station_Code)
print("Station_Lat:", Station_Lat)
print("Station_Long:", Station_Long)
print("Station_Height:", Station_Height)
print("Record_Time:", Record_Time)
print("Sampling_Freq:", Sampling_Freq)
print("Duration:", Duration)
print("Dir_value:", Dir_value)
print("Scale_Factor_Numerator:", Scale_Factor_Numerator)
print("Scale_Factor_Denominator:", Scale_Factor_Denominator)
print("Last_Correction:", Last_Correction)
