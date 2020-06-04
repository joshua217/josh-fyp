
# Initial temperature and parasites
compare(all_data_noSHA['temp_ann'], all_data_noSHA['Smansoni'], 'Annual Average Temperature [°C]', 'Smansoni Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['temp_ann'], all_data_noSHA['hookworm'], 'Annual Average Temperature [°C]', 'Hookworm Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['temp_ann'], all_data_noSHA['ascaris'], 'Annual Average Temperature [°C]', 'Ascaris Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['temp_ann'], all_data_noSHA['trichuris'], 'Annual Average Temperature [°C]', 'Trichuris Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['temp_ann'], all_data_noSHA['other_eggs'], 'Annual Average Temperature [°C]', 'Other STHs Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
hist0plot(all_data_noSHA['temp_ann'], 100, 'Annual Average Temperature in 1673 schools', 0.5, '#08FBF2', 0, [1], ['a'],  'Annual Average Temperature', 'Number of Schools',0)
compare(all_data['temp_ann'], all_data['s.haematobium'], 'Annual Average Temperature [°C]', 'S.Haematobium Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
all_data_noSHA['temp_ann'].mean()
all_data_noSHA['temp_ann'].median()

compare(all_data_noSHA['prec_ann'], all_data_noSHA['Smansoni'], 'Annual Average Precipitation [cm]', 'Smansoni Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['prec_ann'], all_data_noSHA['hookworm'], 'Annual Average Precipitation [cm]', 'Hookworm Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['prec_ann'], all_data_noSHA['ascaris'], 'Annual Average Precipitation [cm]', 'Ascaris Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['prec_ann'], all_data_noSHA['trichuris'], 'Annual Average Precipitation [cm]', 'Trichuris Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['prec_ann'], all_data_noSHA['other_eggs'], 'Annual Average Precipitation [cm]', 'Other STHs Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
hist0plot(all_data_noSHA['prec_ann'], 100, 'Annual Average Temperature in 1673 schools', 0.5, '#08FBF2', 0, [1], ['a'],  'Annual Average Precipitation [cm]', 'Number of Schools',0)
compare(all_data['prec_ann'], all_data['s.haematobium'], 'Annual Average Precipitation [cm]', 'S.Haematobium Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
all_data_noSHA['prec_ann'].mean()
all_data_noSHA['prec_ann'].median()

# Elevation
compare(all_data_noSHA['elevation'], all_data_noSHA['Smansoni'], 'Average Elevation [m]', 'Smansoni Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['elevation'], all_data_noSHA['hookworm'], 'Average Elevation [m]', 'Hookworm Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['elevation'], all_data_noSHA['ascaris'], 'Average Elevation [m]', 'Ascaris Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['elevation'], all_data_noSHA['trichuris'], 'Average Elevation [m]', 'Trichuris Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
compare(all_data_noSHA['elevation'], all_data_noSHA['other_eggs'], 'Average Elevation [m]', 'Other STHs Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
hist0plot(all_data_noSHA['elevation'], 100, 'Average Elevation in 1673 schools', 0.5, '#08FBF2', 0, [1], ['a'],  'Annual Average Precipitation [cm]', 'Number of Schools',0)
compare(all_data['elevation'], all_data['s.haematobium'], 'Average Elevation [m]', 'S.Haematobium Intensity [EPG]', 0, 0, [1, 2], ['Josh'])
print(all_data_noSHA['elevation'].mean())
print(all_data_noSHA['elevation'].median())

