import math
asia = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar (Burma)", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"]
africa = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cape Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Democratic Republic of the Congo", "Republic of the Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "São Tomé and Príncipe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
north_america = ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States of America"]
south_america = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]
europe = ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City"]
oceania = ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]
region = dict()

with open ("js/world-data-2023.csv" , "r")  as f, open("js/emoji.csv", "w") as o:
    asia_count = 0
    africa_count = 0
    north_count = 0
    south_count = 0
    oceania_count = 0
    europe_count = 0
    asia_birth = 0
    africa_birth = 0
    north_birth=0
    south_birth = 0
    oceania_birth = 0
    europe_birth = 0
    
    for line in f:
        
        line = line.strip()
        line = line.split(',')
        country = line[0]
        birth = (line[6])
        if birth.isnumeric():
            birth = float(line[6])
        if birth == 'Birth rate' or birth == '':
            continue
        elif country in asia:
            continent = 'Asia'
            asia_count += 1
            asia_birth += float(birth)

        elif country in africa:
            continent = 'Africa'
            africa_count += 1
            africa_birth += float(birth)
        elif country in north_america:
            continent = 'North America'
            north_count += 1
            north_birth += float(birth)
        elif country in south_america:
            continent = 'South America'
            south_count += 1
            south_birth += float(birth)

        elif country in oceania:
            continent = 'Oceania'
            oceania_count += 1
            oceania_birth += float(birth)
        elif country in europe:
            continent = 'Europe'
            europe_count += 1
            europe_birth += float(birth)
        else:
            continue
        
        new = country +  "," + continent + "," +  str(birth) +'\n'
    asia_avg = asia_birth/asia_count
    africa_avg = africa_birth/africa_count
    north_avg = north_birth/north_count
    south_avg = south_birth/south_count
    oceania_avg = oceania_birth/oceania_count
    europe_avg = europe_birth/europe_count
    region['Asia'] = math.ceil(asia_avg)
    region['Africa'] = math.ceil(africa_avg)
    region['North America'] = math.ceil(north_avg)
    region['South America'] = math.ceil(south_avg)
    region['Oceania'] = math.ceil(oceania_avg)
    region['Europe'] = math.ceil(europe_avg)
    for c in region:
        for i in range(region[c]):
            k = c + ',' + 'x' + '\n'
            o.write(k)