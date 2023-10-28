import numpy as np
import pandas as pd
from datetime import datetime
import yfinance as yf

tickers = ["RUSTA.ST", "SEAF.ST", "SEDANA.ST", "EMBRAC-B.ST", "CS.ST",
           "ACRI-B.ST", "VESTUM.ST", "ALLEI.ST", "SYNACT.ST", "ENGCON-B.ST",
           "EMIL-B.ST", "VEFAB.ST", "NICA.ST", "OX2.ST",
           "MMGR-B.ST", "SLP-B.ST", "MANG.ST", "NORVA.ST", "TDVOX.ST",
           "NIVI-B.ST", "KLARA-B.ST", "SFAB.ST", "SYNSAM.ST", "VOLCAR-B.ST",
           "ISOFOL.ST", "NETEL.ST", "BFG.ST", "NORB-B.ST", "TRUE-B.ST",
           "STOR-B.ST", "TRANS.ST", "FASTAT.ST", "PRFO.ST",
           "SEZI.ST", "INFREA.ST", "CPAC-SPAC.ST", "RVRC.ST",
           "SDIP-B.ST", "SIVE.ST", "SLEEP.ST", "MILDEF.ST", "CIBUS.ST",
           "LINC.ST", "SF.ST", "ARPL.ST", "HEM.ST", "OVZON.ST", "PIERCE.ST",
           "YUBICO.ST", "CINT.ST", "TRIAN-B.ST", "MAHA-A.ST", "ANNE-B.ST",
           "FG.ST", "SAVE.ST", "NPAPER.ST", "WBGR-B.ST", "QLIRO.ST",
           "IRLAB-A.ST", "READ.ST", "GPG.ST", "IRRAS.ST", "BICO.ST",
           "XSPRAY.ST", "EPRO-B.ST", "KFAST-B.ST", "SBB-B.ST", "EGTX.ST",
           "VICO.ST", "XBRANE.ST", "8TRA.ST", "K2A-B.ST", "JOMA.ST",
           "GREEN.ST", "KAR.ST", "VPLAY-B.ST", "HANZA.ST",
           "ACE.ST", "QLINEA.ST", "LIME.ST", "NYF.ST",
           "BRIN-B.ST", "CANTA.ST", "IBT-B.ST", "CALTX.ST", "PENG-B.ST",
           "EPI-B.ST", "IPCO.ST", "BETCO.ST", "NCAB.ST",
           "STEF-B.ST", "NIL-B.ST", "IMMNOV.ST", "RAIL.ST", "BHG.ST",
           "IMMU.ST"]

ipo_date = ["19 oktober 2023", "11 maj 2023", "25 januari 2023",
            "22 december 2022", "19 december 2022", "16 december 2022",
            "13 december 2022", "31 augusti 2022", "12 juli 2022",
            "17 juni 2022", "13 juni 2022", "1 juni 2022",
            "29 mars 2022",
            "6 april 2022", "31 mars 2022", "23 mars 2022", "24 februari 2022",
            "9 december 2021", "9 december 2021", "3 december 2021",
            "2 december 2021", "1 december 2021", "29 oktober 2021",
            "29 oktober 2021", "21 oktober 2021", "15 oktober 2021",
            "15 oktober 2021", "12 oktober 2021", "8 oktober 2021",
            "6 oktober 2021", "29 september 2021",
            "16 september 2021", "1 juli 2021", "30 juni 2021",
            "29 juni 2021", "23 juni 2021", "16 juni 2021",
            "11 juni 2021", "10 juni 2021", "8 juni 2021", "4 juni 2021",
            "1 juni 2021", "28 maj 2021", "26 maj 2021", "25 maj 2021",
            "27 april 2021", "20 april 2021", "26 mars 2021", "25 mars 2021",
            "19 februari 2021", "17 december 2020", "17 december 2020",
            "11 december 2020", "9 december 2020", "25 november 2020",
            "22 oktober 2020", "13 oktober 2020", "2 oktober 2020",
            "30 september 2020", "17 september 2020", "30 juni 2020",
            "20 maj 2020", "20 april 2020", "27 mars 2020", "23 mars 2020",
            "29 november 2019", "20 september 2019", "31 oktober 2019",
            "27 september 2019", "23 september 2019",
            "28 juni 2019", "20 juni 2019", "5 juni 2019", "16 april 2019",
            "11 april 2019", "28 mars 2019", "25 mars 2019",
            "13 mars 2019", "7 december 2018", "6 december 2018",
            "23 november 2018", "27 september 2018",
            "25 september 2018", "10 september 2018", "29 juni 2018",
            "19 juni 2018", "18 juni 2018", "8 juni 2018", "8 juni 2018",
            "5 juni 2018", "10 april 2018", "4 april 2018", "3 april 2018",
            "3 april 2018", "27 mars 2018", "15 januari 2018"]

print(len(tickers))
print(len(ipo_date))

# Swedish to Egnlish mapping
swedish_to_english = {
        'januari': 'January', 'februari': 'February', 'mars': 'March',
        'april': 'April', 'maj': 'May', 'juni': 'June', 'juli': 'July',
        'augusti': 'August', 'september': 'September', 'oktober': 'October',
        'november': 'November', 'december': 'December'
        }


# Function to convert dates to yyyy-mm-dd
def convert_date(swedish_date):
    # Replace Swedish month names with English month names
    for swedish, english in swedish_to_english.items():
        swedish_date = swedish_date.replace(swedish, english)
    # Parse and reformat the date
    date_obj = datetime.strptime(swedish_date, '%d %B %Y')
    return date_obj.strftime('%Y-%m-%d')


# Create a list of the converted dates
f_ipo_date = [convert_date(date) for date in ipo_date]

# Increase the display options
pd.options.display.max_rows = None
pd.options.display.max_columns = None

# Create a dataframe
dataframe = pd.DataFrame({'Ticker': tickers, 'ipo_date': f_ipo_date})
print(dataframe)


# Function to download the data
def download_data(ticker, date):
    start_date = pd.to_datetime(date)
    end_date = start_date + pd.Timedelta(days=1)  # The next day

    # Format dates to string for yfinance
    start_str = start_date.strftime('%Y-%m-%d')
    end_str = end_date.strftime('%Y-%m-%d')

    # Download data
    data = yf.download(ticker, start=start_str, end=end_str)
    return data


# Create empty lists
opens = []
highs = []
lows = []
closes = []
adj_closes = []
volumes = []

# Download and append the data
for ticker, date in zip(tickers, f_ipo_date):
    print(f'Downloading data for {ticker} on {date}')
    data = download_data(ticker, date)
    if not data.empty:  # Check if data is not empty
        # Append the stock data to the lists
        opens.append(data['Open'].values[0])
        highs.append(data['High'].values[0])
        lows.append(data['Low'].values[0])
        closes.append(data['Close'].values[0])
        adj_closes.append(data['Adj Close'].values[0])
        volumes.append(data['Volume'].values[0])
    else:
        # Append NaN if data is empty
        opens.append(np.nan)
        highs.append(np.nan)
        lows.append(np.nan)
        closes.append(np.nan)
        adj_closes.append(np.nan)
        volumes.append(np.nan)

# Add the stock data to the dataframe
dataframe['Open'] = opens
dataframe['High'] = highs
dataframe['Low'] = lows
dataframe['Close'] = closes
dataframe['Adj Close'] = adj_closes
dataframe['Volume'] = volumes

# Print
print(dataframe)

# Save
dataframe.to_csv('data.csv', index=False)
