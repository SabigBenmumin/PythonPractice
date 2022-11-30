def leaps():
    leaps_years = ''
    begin_y = int(input("Begin Year: "))
    end_y = int(input("End Year: "))
    for year in range(begin_y,end_y+1):
        if (((year-543) % 4 == 0) and ((year-543) % 100 != 0)) or ((year-543) % 400 == 0):
            leaps_years += f"{year}, "
    years = leaps_years.rstrip(", ")
    print(f"Leap Years from {begin_y} to {end_y}: {years}")

leaps()
