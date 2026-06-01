import pandas as pd
import os

def generate_132_countries_dataset(filepath):
    """
    Automatically generates a continuous year-by-year global dataset (2000-2026)
    with exactly 132 countries across the 6 official WHO Regions.
    """
    # 47 African Region Countries
    afr = ("Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cabo Verde", "Central African Republic", "Chad", "Comoros", "Congo", "Cote d'Ivoire", "DR Congo", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "South Africa", "South Sudan", "Togo", "Uganda", "Tanzania", "Zambia", "Zimbabwe")
    
    # 25 Americas Region Countries
    amr = ("Argentina", "Belize", "Bolivia", "Brazil", "Colombia", "Costa Rica", "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "French Guiana", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Suriname", "Bahamas", "Chile", "Venezuela")
    
    # 15 Eastern Mediterranean Region Countries
    emr = ("Afghanistan", "Djibouti", "Egypt", "Iran", "Iraq", "Jordan", "Libya", "Morocco", "Oman", "Pakistan", "Saudi Arabia", "Somalia", "Sudan", "Syria", "Yemen")
    
    # 11 South-East Asia Region Countries
    sear = ("Bangladesh", "Bhutan", "DPR Korea", "India", "Indonesia", "Maldives", "Myanmar", "Nepal", "Sri Lanka", "Thailand", "Timor-Leste")
    
    # 19 Western Pacific Region Countries
    wpr = ("Cambodia", "China", "Fiji", "Kiribati", "Lao PDR", "Malaysia", "Marshall Islands", "Micronesia", "New Zealand", "Palau", "Papua New Guinea", "Philippines", "Republic of Korea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu", "Vietnam")
    
    # 15 European Region Countries
    eur = ("Georgia", "Turkey", "Tajikistan", "Azerbaijan", "Uzbekistan", "Kyrgyzstan", "Armenia", "Turkmenistan", "Russian Federation", "Albania", "Bosnia and Herzegovina", "Montenegro", "North Macedonia", "Serbia", "Ukraine")

    rows = list()
    
    # Loop generates continuous yearly profiles from 2000 to 2026 (No gaps)
    for year in range(2000, 2027):
        # 1. Africa
        for country in afr:
            seed_val = sum(map(ord, country))
            base = (seed_val % 400 + 80) * 1000
            cases = int(base * (1.3 - 0.015 * (year - 2000)))
            deaths = int(cases * 0.005)
            nets = int(cases * 0.8)
            rows.append(dict(Year=year, Country=country, WHO_Region="Africa", Reported_Confirmed_Cases=cases, Estimated_Cases_WHO=int(cases*1.5), Reported_Deaths=deaths, Estimated_Deaths_WHO=int(deaths*1.2), Plasmodium_Vivax_Pct=15.0, Rainfall_Anomaly_mm=25.4, Bednets_Distributed=nets))
            
        # 2. Americas
        for country in amr:
            seed_val = sum(map(ord, country))
            base = (seed_val % 90 + 9) * 1000
            cases = int(base * (1.1 - 0.02 * (year - 2000)))
            deaths = int(cases * 0.001)
            nets = int(cases * 0.6)
            rows.append(dict(Year=year, Country=country, WHO_Region="Americas", Reported_Confirmed_Cases=cases, Estimated_Cases_WHO=int(cases*1.3), Reported_Deaths=deaths, Estimated_Deaths_WHO=int(deaths*1.1), Plasmodium_Vivax_Pct=85.0, Rainfall_Anomaly_mm=-5.2, Bednets_Distributed=nets))
            
        # 3. Eastern Mediterranean (with flood spike simulations for Pakistan and Sudan)
        for country in emr:
            seed_val = sum(map(ord, country))
            base = (seed_val % 150 + 15) * 1000
            spike = 5.0 if year in (2022, 2023) and country in ("Pakistan", "Sudan") else 1.0
            cases = int(base * (1.2 - 0.01 * (year - 2000)) * spike)
            deaths = int(cases * 0.002)
            nets = int(cases * 0.7)
            rows.append(dict(Year=year, Country=country, WHO_Region="Eastern Mediterranean", Reported_Confirmed_Cases=cases, Estimated_Cases_WHO=int(cases*1.4), Reported_Deaths=deaths, Estimated_Deaths_WHO=int(deaths*1.2), Plasmodium_Vivax_Pct=79.0, Rainfall_Anomaly_mm=85.6, Bednets_Distributed=nets))
            
        # 4. South-East Asia
        for country in sear:
            seed_val = sum(map(ord, country))
            base = (seed_val % 250 + 25) * 1000
            cases = int(base * (1.4 - 0.03 * (year - 2000)))
            deaths = int(cases * 0.003)
            nets = int(cases * 0.9)
            rows.append(dict(Year=year, Country=country, WHO_Region="South-East Asia", Reported_Confirmed_Cases=cases, Estimated_Cases_WHO=int(cases*1.6), Reported_Deaths=deaths, Estimated_Deaths_WHO=int(deaths*1.3), Plasmodium_Vivax_Pct=48.0, Rainfall_Anomaly_mm=12.4, Bednets_Distributed=nets))
            
        # 5. Western Pacific
        for country in wpr:
            seed_val = sum(map(ord, country))
            base = (seed_val % 120 + 12) * 1000
            cases = int(base * (1.0 - 0.01 * (year - 2000)))
            deaths = int(cases * 0.001)
            nets = int(cases * 0.5)
            rows.append(dict(Year=year, Country=country, WHO_Region="Western Pacific", Reported_Confirmed_Cases=cases, Estimated_Cases_WHO=int(cases*1.2), Reported_Deaths=deaths, Estimated_Deaths_WHO=int(deaths*1.1), Plasmodium_Vivax_Pct=55.0, Rainfall_Anomaly_mm=4.1, Bednets_Distributed=nets))
            
        # 6. Europe (Eliminated territory simulation)
        for country in eur:
            seed_val = sum(map(ord, country))
            base = (seed_val % 8 + 1) * 10
            cases = int(base * (0.8 - 0.03 * (year - 2000)))
            deaths = 0
            nets = 0
            rows.append(dict(Year=year, Country=country, WHO_Region="Europe", Reported_Confirmed_Cases=cases, Estimated_Cases_WHO=int(cases*1.1), Reported_Deaths=deaths, Estimated_Deaths_WHO=0, Plasmodium_Vivax_Pct=99.0, Rainfall_Anomaly_mm=1.1, Bednets_Distributed=nets))

    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)

def load_and_clean_data(filepath):
    """
    Loads global dataset. Automatically executes creation script if file is missing.
    """
    if not os.path.exists(filepath):
        generate_132_countries_dataset(filepath)
        
    try:
        df = pd.read_csv(filepath)
        df.columns = df.columns.str.strip()
        
        df = df.assign(Country=df.Country.astype(str))
        df = df.assign(WHO_Region=df.WHO_Region.astype(str))
        
        clean_types = dict(
            Year=int,
            Reported_Confirmed_Cases=int,
            Estimated_Cases_WHO=int,
            Reported_Deaths=int,
            Estimated_Deaths_WHO=int,
            Bednets_Distributed=int
        )
        df = df.astype(clean_types)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def apply_dashboard_filters(df, selected_regions, selected_countries, year_range):
    """
    Applies filters dynamically for global dashboard using bracket-free queries.
    """
    if df.empty:
        return df
        
    if selected_regions:
        df = df.query("WHO_Region in @selected_regions")
        
    if selected_countries:
        df = df.query("Country in @selected_countries")
        
    start_year, end_year = year_range
    df = df.query("Year >= @start_year and Year <= @end_year")
    
    return df
