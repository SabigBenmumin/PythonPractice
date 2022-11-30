def leaps(BY,EY):
    years = ''
    have_leap_year = False
    for year in range(BY,EY+1):
        if (((year-543) % 4 == 0) & ((year-543) % 100 != 0)) or ((year-543) % 400 == 0):
            years += f"{year}, "
            have_leap_year = True
    result = years.rstrip(", ")
    return result, have_leap_year

def main():
    begin_year = int(input("Begin Year: "))
    end_year = int(input("End Year: "))
    leap_years = leaps(begin_year,end_year)
    if leap_years[1]:
        print(f"leap yeas from {begin_year} to {end_year}: {leap_years[0]}")
    else:
        print(f"leap yeas from {begin_year} to {end_year}: None")
main()