# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
updated_damages = []
for dmg in damages:
  if dmg == 'Damages not recorded':
    updated_damages.append(dmg)
  elif dmg.find('M') != -1:
    updated_damages.append(float(dmg.split('M')[0])*conversion['M'])
  else:
    updated_damages.append(float(dmg.split('B')[0])*conversion['B'])
# test function by updating damages
print(updated_damages)

# 2 
# Create a Table
def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricanes = {}
  length = len(names)
  for i in range(length):
    hurricanes[names[i]] = {'Name': names[i],
    'Month': months[i],
    'Year': years[i],
    'Max Sustained Wind': max_sustained_winds[i],
    'Areas Affected': areas_affected[i],
    'Damage': updated_damages[i],
    'Deaths': deaths[i]
    }
  return hurricanes
# Create and view the hurricanes dictionary
new_hurricanes_list = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print(new_hurricanes_list)
# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def hurricane_year(hurricanes):
  hurricane_year = {}
  for cane in hurricanes:
    current_year = hurricanes[cane]['Year']
    current_cane = hurricanes[cane]
    if current_year not in hurricane_year:
      hurricane_year[current_year] = [current_cane]
    else:
      hurricane_year[current_year].append(current_cane)
  return hurricane_year

hurricanes_by_year = hurricane_year(new_hurricanes_list)
print(hurricanes_by_year[1932])
# 4
# Counting Damaged Areas
def count_damaged_areas(hurricanes):
  damagedCount = {}
  for cane in hurricanes:
    for area in hurricanes[cane]['Areas Affected']:
      if area not in damagedCount:
        damagedCount[area] = 1
      else:
        damagedCount[area] += 1
  return damagedCount

# create dictionary of areas to store the number of hurricanes involved in
affectedareascount = count_damaged_areas(new_hurricanes_list)
print(affectedareascount)

# 5 
# Calculating Maximum Hurricane Count
def maxdamage(hurricanes):
  max_area = ''
  max_area_count = 0
  for area in hurricanes:
    if max_area_count < hurricanes[area]:
      max_area = area
      max_area_count = hurricanes[area]
  return max_area, max_area_count


# find most frequently affected area and the number of hurricanes involved in
maximumDmg = maxdamage(affectedareascount)
print(maximumDmg)


# 6
# Calculating the Deadliest Hurricane
def maxdeath(hurricanes):
  maxdeatharea = ''
  maxdeathcount = 0
  for area in hurricanes:
    if maxdeathcount < hurricanes[area]['Deaths']:
      maxdeatharea = area
      maxdeathcount = hurricanes[area]['Deaths']
  return maxdeatharea, maxdeathcount

# find highest mortality hurricane and the number of deaths
deatharea, deathcount = maxdeath(new_hurricanes_list)
print(deatharea, deathcount)
# 7
# Rating Hurricanes by Mortality
def mortalityrating(hurricanes):
  hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for area in hurricanes:
    if hurricanes[area]['Deaths'] == 0:
      hurricanes_by_mortality[0].append(hurricanes[area])
    elif hurricanes[area]['Deaths'] <= 100:
      hurricanes_by_mortality[1].append(hurricanes[area])
    elif hurricanes[area]['Deaths'] <= 500:
      hurricanes_by_mortality[2].append(hurricanes[area])
    elif hurricanes[area]['Deaths'] <= 1000:
      hurricanes_by_mortality[3].append(hurricanes[area])
    elif hurricanes[area]['Deaths'] <= 10000:
      hurricanes_by_mortality[4].append(hurricanes[area])
    else:
      hurricanes_by_mortality[5].append(hurricanes[area])
  return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
mortalityhurricanes = mortalityrating(new_hurricanes_list)
print(mortalityhurricanes[5])


# 8 Calculating Hurricane Maximum Damage
def maxcostly(hurricanes):
  maxcostlycane = ''
  maxcost = 0
  for cane in hurricanes:
    if hurricanes[cane]['Damage'] == 'Damages not recorded':
      pass
    elif maxcost < hurricanes[cane]['Damage']:
      maxcostlycane = cane
      maxcost = hurricanes[cane]['Damage']
  return maxcostlycane, maxcost
# find highest damage inducing hurricane and its total cost
maxcostcane, maxcost = maxcostly(new_hurricanes_list)
print(maxcostcane, maxcost)

# 9
# Rating Hurricanes by Damage
def damagescale(hurricanes):
  damage_scale = {0: 0,
                  1: 100000000,
                  2: 1000000000,
                  3: 10000000000,
                  4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes:
    if hurricanes[cane]['Damage'] == 'Damages not recorded':
      pass
    elif hurricanes[cane]['Damage'] <= damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes[cane])
    elif hurricanes[cane]['Damage'] > damage_scale[0] and hurricanes[cane]['Damage'] <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[cane])
    elif hurricanes[cane]['Damage'] > damage_scale[1] and hurricanes[cane]['Damage'] <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[cane])
    elif hurricanes[cane]['Damage'] > damage_scale[2] and hurricanes[cane]['Damage'] <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[cane])
    elif hurricanes[cane]['Damage'] > damage_scale[3] and hurricanes[cane]['Damage'] <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[cane])
    else:
      hurricanes_by_damage[5].append(hurricanes[cane])
  return hurricanes_by_damage
# categorize hurricanes in new dictionary with damage severity as key
maxdamagecane = damagescale(new_hurricanes_list)
print(maxdamagecane[5])
