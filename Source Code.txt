import pandas as pd
path = r"C:\Users\Jules\Desktop\New folder\unnati_phase1_data_revised.csv"
df = pd.read_csv(path)
print(df.shape)
print(df.describe())
print(df.query('Alert=="cas_fcw"'))
print(df.query('Alert=="cas_hmw"'))
print(df.query('Alert=="cas_ldw"'))
print(df.query('Alert=="cas_pcw"'))
df['Alert'].value_counts()
df.groupby('Alert')['Speed']\.agg(['mean'])
df.groupby('Vehicle')['Speed']\.agg(['mean'])
df['Vehicle'].value_counts()
df['Alert'].value_counts(normalize=True)
df[(df['Alert']=="cas_hmw") & (df['Vehicle']==805)]
df[(df['Alert']=="cas_pcw") & (df['Vehicle']==805)]
df[(df['Alert']=="cas_fcw") & (df['Vehicle']==805)]
df[(df['Alert']=="cas_ldw") & (df['Vehicle']==805)]
df[(df['Alert']=="cas_fcw") & (df['Vehicle']==2846)]
df[(df['Alert']=="cas_hmw") & (df['Vehicle']==2846)]
df[(df['Alert']=="cas_ldw") & (df['Vehicle']==2846)]
df[(df['Alert']=="cas_fcw") & (df['Vehicle']==3143)]
df[(df['Alert']=="cas_pcw") & (df['Vehicle']==3143)]
df[(df['Alert']=="cas_ldw") & (df['Vehicle']==3143)]
df[(df['Alert']=="cas_fcw") & (df['Vehicle']==5339)]
df[(df['Alert']=="cas_pcw") & (df['Vehicle']==5339)]
df[(df['Alert']=="cas_hmw") & (df['Vehicle']==5339)]
df[(df['Alert']=="cas_ldw") & (df['Vehicle']==5339)]
df[(df['Time']>="06:00:00") & (df['Time']<="09:00:00")].value_counts()
