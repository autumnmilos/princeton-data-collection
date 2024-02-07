from google_scholar_py import CustomGoogleScholarProfiles
import json

#This file directs profile_results.py to scrape all of the profile links from the input file

# python3 custom.py > profilepage.json

obj = ''
error_names = []
input_filename = 'sampleinput.txt'

#def remove_line_after_empty_line(input_filename):
with open(input_filename, 'r') as infile:
    lines = infile.readlines()

output_lines = []
for line in lines:
    if line.strip():
        obj = line.strip()
        parser = CustomGoogleScholarProfiles()
        data = parser.scrape_google_scholar_profiles(
            query=obj,
            pagination=False,
            save_to_csv=False,
            save_to_json=False,
        )
        if len(data) == 0:
            error_names.append(obj)
        else:
            entry = data[0]
            # print('Name:', entry['name'])
            print(json.dumps(entry, indent=2))
    else:
        print()




#Print this to see which names were not found
# print("\n\nNames not found:")
# for name in error_names:
#     if len(name) == 0:
#         pass
#     else:
#         print(name)

