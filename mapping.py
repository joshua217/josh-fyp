import geopandas as gpd
import geoplot
from matplotlib import pyplot as plt
from shapely.geometry import Point, Polygon, linestring
import numpy as np
import pandas as pd
import shapefile as shp
import seaborn as sns


def prev_mapping(map_data, col_name, title):
    woreda_path = r"C:\dev\data\josh-fyp\inputs\ETH_admin_SHP\ETH.shp"
    woreda = gpd.read_file(woreda_path)
    # 'init': 'epsg:32637'
    river_path = r"C:\dev\data\josh-fyp\inputs\eth_rivers\eth_rivers.shp"
    rivers = gpd.read_file(river_path)
    rivers.crs = {'init': 'epsg:32637'}
    rivers = rivers.to_crs('epsg:4326')

    watershed_path = r"C:\dev\data\josh-fyp\inputs\eth_watshed\eth_watshed.shp"
    watshed = gpd.read_file(watershed_path)
    watshed.crs = {'init': 'epsg:32637'}
    watshed = watshed.to_crs('epsg:4326')

    lake_path = r"C:\dev\data\josh-fyp\inputs\Eth_GIS\ETH_LAKE.SHP"
    lakes = gpd.read_file(lake_path)
    lakes.crs = {'init': 'epsg:32637'}
    lakes = lakes.to_crs('epsg:4326')

    crs = {'init': 'epsg:4326'}

    ethiopia = woreda

    sch_geo = map_data[['Long', 'Lat']]
    geometry = [Point(xy) for xy in zip(sch_geo['Long'], sch_geo['Lat'])]

    geothiopia = gpd.GeoDataFrame(map_data, crs=crs, geometry = geometry)
    labels = ('Low <10%', 'High >10%')

    fig, ax = plt.subplots(figsize = (15, 15))
    gplt.polyplot(ethiopia, ax=ax)
    # geothiopia[geothiopia[col_name] >= 0].plot(ax=ax, markersize=2, color="orange", marker="o",
    #                                            label="0 % < Prevalence < 10 %")
    # ethiopia.plot(ax=ax, color='xkcd:really light blue')   # gplt.polyplot(ethiopia) # xkcd: ice
    geothiopia[geothiopia[col_name] == 0].plot(ax=ax, markersize=3, color="yellow", marker="o", label="0% Prev")
    geothiopia[geothiopia[col_name] >= 0].plot(ax=ax, markersize=5, color="orange", marker="o", label="0 % < Prevalence < 10 %")
    geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    plt.title(title)
    plt.legend(labels)
    plt.savefig(r"C:\dev\data\josh-fyp\outputs\mapping\Prevalence\{}_ethiopia.png".format(col_name))
    # plt.show()

    fig, ax = plt.subplots(figsize = (15, 15))
    rivers.plot(ax=ax)
    # geothiopia[geothiopia[col_name] == 0].plot(ax=ax, markersize=5, color="white", marker="o", label="0% Prev")
    # geothiopia[geothiopia[col_name] >= 0].plot(ax=ax, markersize=5, color="green", marker="o", label="0 % < Prevalence < 10 %")
    # geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    geothiopia[geothiopia[col_name] >= 0].plot(ax=ax, markersize=5, color="orange", marker="o", label="0 % < Prevalence < 10 %")
    geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    plt.title(title + " on rivers")
    plt.legend(labels)
    plt.savefig(r"C:\dev\data\josh-fyp\outputs\mapping\Prevalence\{}_rivers.png".format(col_name))

    fig, ax = plt.subplots(figsize = (15, 15))
    watshed.plot(ax=ax)
    # geothiopia[geothiopia[col_name] == 0].plot(ax=ax, markersize=5, color="white", marker="o", label="0% Prev")
    # geothiopia[geothiopia[col_name] >= 0].plot(ax=ax, markersize=5, color="green", marker="o", label="0 % < Prevalence < 10 %")
    # geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    geothiopia[geothiopia[col_name] >= 0].plot(ax=ax, markersize=5, color="orange", marker="o", label="0 % < Prevalence < 10 %")
    geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    plt.title(title + " on watersheds")
    plt.legend(labels)
    plt.savefig(r"C:\dev\data\josh-fyp\outputs\mapping\Prevalence\{}_watshed.png".format(col_name))

    fig, ax = plt.subplots(figsize = (15, 15))
    lakes.plot(ax=ax)
    # geothiopia[geothiopia[col_name] == 0].plot(ax=ax, markersize=5, color="white", marker="o", label="0% Prev")
    # geothiopia[geothiopia[col_name] >= 0].plot(ax=ax, markersize=5, color="green", marker="o", label="0 % < Prevalence < 10 %")
    # geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    geothiopia[geothiopia[col_name] >= 0].plot(ax=ax, markersize=5, color="orange", marker="o", label="0 % < Prevalence < 10 %")
    geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    plt.title(title + " on watersheds")
    plt.legend(labels)
    plt.savefig(r"C:\dev\data\josh-fyp\outputs\mapping\Prevalence\{}_watshed.png".format(col_name))

    plt.figure()
    plt.hist(geothiopia[col_name], bins=100)
    plt.suptitle('Histogram of ' + col_name)
    plt.ylabel(col_name)
    a = np.count_nonzero(map_data[col_name])
    b = np.size(map_data[col_name])
    plt.title(r"Total Schools: {} Zero %: {} Non-zero %: {}".format(b, b - a, a))
    plt.savefig(r"C:\dev\data\josh-fyp\outputs\mapping\Prevalence\{}_histogram.png".format(col_name))
    # plt.show()

def int_mapping(map_data, col_name, title):
    woreda_path = r"C:\dev\data\josh-fyp\inputs\ETH_admin_SHP\ETH.shp"
    watershed_path = r"C:\dev\data\josh-fyp\inputs\eth_watshed\eth_watshed.shp"
    lake_path = r"C:\dev\data\josh-fyp\inputs\Eth_GIS\ETH_LAKE.SHP"
    rivers_path = r"C:\dev\data\josh-fyp\inputs\Eth_GIS\eth_rivers.shp"     # 'init': 'epsg:32637'
    rivers = gpd.read_file(r"C:\dev\data\josh-fyp\inputs\eth_rivers\eth_rivers.shp")
    # r"C:\dev\data\josh-fyp\inputs\Eth_GIS\eth_rivers.shp")
    rivers.crs = {'init': 'epsg:32637'}
    rivers = rivers.to_crs('epsg:4326')
    watshed = gpd.read_file(watershed_path)
    watshed.crs = {'init': 'epsg:32637'}
    watshed = watshed.to_crs('epsg:4326')

    shp_2_path = r"C:\dev\data\josh-fyp\inputs\Eth_GIS\eth_basins_new.shp"
    woreda = gpd.read_file(woreda_path)
    crs = {'init': 'epsg:4326'}

    # dummy = dummy.rename(columns={'Woreda':'OBJECTID'})
    # ethiopia = ethiopia.merge(dummy, on='OBJECTID')

    ethiopia = woreda
    # sch
    sch_geo = map_data[['Long', 'Lat']]
    geometry = [Point(xy) for xy in zip( sch_geo['Long'], sch_geo['Lat'])]

    geothiopia = gpd.GeoDataFrame(map_data, crs = crs, geometry = geometry)
    labels = ('Low <10%', 'High >10%')

    fig, ax = plt.subplots(figsize = (15, 15))
    ethiopia.plot(ax=ax, color='xkcd:really light blue')   # gplt.polyplot(ethiopia) # xkcd: ice
    # geothiopia[geothiopia[col_name] == 0].plot(ax=ax, markersize=3, color="yellow", marker="o", label="0% Prev")
    geothiopia[geothiopia[col_name] > 0].plot(ax=ax, markersize=5, color="orange", marker="o", label="0 % < Prevalence < 10 %")
    geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    plt.title(title)
    plt.legend(labels)
    plt.savefig(r"C:\dev\data\josh-fyp\outputs\mapping\Intensity\{}_ethiopia.png".format(col_name))
    # plt.show()

    fig, ax = plt.subplots(figsize = (15, 15))
    rivers.plot(ax=ax)
    # geothiopia[geothiopia[col_name] == 0].plot(ax=ax, markersize=5, color="white", marker="o", label="0% Prev")
    # geothiopia[geothiopia[col_name] >= 0].plot(ax=ax, markersize=5, color="green", marker="o", label="0 % < Prevalence < 10 %")
    # geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    geothiopia[geothiopia[col_name] > 0].plot(ax=ax, markersize=5, color="orange", marker="o", label="0 % < Prevalence < 10 %")
    geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    plt.title(title + " on rivers")
    plt.legend(labels)
    plt.savefig(r"C:\dev\data\josh-fyp\outputs\mapping\Intensity\{}_rivers.png".format(col_name))
    # plt.show()

    fig, ax = plt.subplots(figsize = (15, 15))
    watshed.plot(ax=ax)
    # geothiopia[geothiopia[col_name] == 0].plot(ax=ax, markersize=5, color="white", marker="o", label="0% Prev")
    # geothiopia[geothiopia[col_name] >= 0].plot(ax=ax, markersize=5, color="green", marker="o", label="0 % < Prevalence < 10 %")
    # geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    geothiopia[geothiopia[col_name] > 0].plot(ax=ax, markersize=5, color="orange", marker="o", label="0 % < Prevalence < 10 %")
    geothiopia[geothiopia[col_name] >= 0.1].plot(ax=ax, markersize=5, color="red", marker="o", label=">10%")
    plt.title(title + " on watersheds")
    plt.legend(labels)
    plt.savefig(r"C:\dev\data\josh-fyp\outputs\mapping\Intensity\{}_watshed.png".format(col_name))
    # plt.show()

    plt.figure()
    plt.hist(geothiopia[col_name], bins=100)
    plt.suptitle('Histogram of ' + col_name)
    plt.ylabel(col_name)
    a = np.count_nonzero(map_data[col_name])
    b = np.size(map_data[col_name])
    plt.title(r"Total Schools: {} Zero %: {} Non-zero %: {}".format(b, b - a, a))
    plt.savefig(r"C:\dev\data\josh-fyp\outputs\mapping\Intensity\{}_histogram.png".format(col_name))
    # plt.show()

    # 3-d plot
    # logis_regre['size'] = 0.1
    # #Prev
    # logis_regre['c_mansoni'] = '#BEEEE3'
    # mask = logis_regre.trichuris > 0
    # logis_regre.loc[mask, 'c_mansoni'] = '#D53A00'
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax = plt.scatter(logis_regre['Lat'], logis_regre['Long'], zs=logis_regre['elevation'], c=logis_regre['c_mansoni'], s=5)

def mapping_contiuous(all_data_noSHA):
    woreda = gpd.read_file(r"C:\dev\data\josh-fyp\inputs\ETH_admin_SHP\ETH.shp")
    # 'init': 'epsg:32637'
    rivers = gpd.read_file(r"C:\dev\data\josh-fyp\inputs\eth_rivers\eth_rivers.shp")
    rivers.crs = {'init': 'epsg:32637'}
    rivers = rivers.to_crs('epsg:4326')

    watshed = gpd.read_file(r"C:\dev\data\josh-fyp\inputs\eth_watshed\eth_watshed.shp")
    watshed.crs = {'init': 'epsg:32637'}
    watshed = watshed.to_crs('epsg:4326')

    lakes = gpd.read_file(r"C:\dev\data\josh-fyp\inputs\Eth_GIS\ETH_LAKE.SHP")
    lakes.crs = {'init': 'epsg:32637'}
    lakes = lakes.to_crs('epsg:4326')

    crs = {'init': 'epsg:4326'}
    sch_geo = all_data_noSHA[['Long', 'Lat']]
    geometry = [Point(xy) for xy in zip(sch_geo['Long'], sch_geo['Lat'])]



sns.set(style='whitegrid', palette='pastel', color_codes=True)
sns.mpl.rc('figure', figsize=(10,6))

#opening the vector map
shp_path = woreda_path
shp_path_test = r"C:\dev\data\josh-fyp\inputs\test_mapping\District_Boundary.shp"

#reading the shape file by using reader function of the shape lib
sf = shp.Reader(shp_path)

# Number of different Shapes imported
len(sf.shapes())
# To explore those records
sf.records()
# To explore a particular record where 1 is the Id or row number and 0 refers to the column

# Convert to pd.DataFrame
def read_shapefile(sf):
    #fetching the headings from the shape file
    fields = [x[0] for x in sf.fields][1:]
#fetching the records from the shape file
    records = [list(i) for i in sf.records()]
    shps = [s.points for s in sf.shapes()]
#converting shapefile data into pandas dataframe
    df = pd.DataFrame(columns=fields, data=records)
#assigning the coordinates
    df = df.assign(coords=shps)
    return df

df = read_shapefile(sf)
# df.shape (575, 19)

def plot_shape(id, s=None):
    plt.figure()
    #plotting the graphical axes where map ploting will be done
    ax = plt.axes()
    ax.set_aspect('equal')
#storing the id number to be worked upon
    shape_ex = sf.shape(id)
#NP.ZERO initializes an array of rows and column with 0 in place of each elements
    #an array will be generated where number of rows will be(len(shape_ex,point))and number of columns will be 1 and stored into the variable
    x_lon = np.zeros((len(shape_ex.points),1))
#an array will be generated where number of rows will be(len(shape_ex,point))and number of columns will be 1 and stored into the variable
    y_lat = np.zeros((len(shape_ex.points),1))
    for ip in range(len(shape_ex.points)):
        x_lon[ip] = shape_ex.points[ip][0]
        y_lat[ip] = shape_ex.points[ip][1]
#plotting using the derived coordinated stored in array created by numpy
    plt.plot(x_lon,y_lat)
    x0 = np.mean(x_lon)
    y0 = np.mean(y_lat)
    plt.text(x0, y0, s, fontsize=10)
# use bbox (bounding box) to set plot limits
    plt.xlim(shape_ex.bbox[0],shape_ex.bbox[2])
    return x0, y0

# set the filepath and load
#reading the file stored in variable fp
map_df = gpd.read_file(woreda_path)

# map_df.head()
# map_df.plot()
# Match Jacks Woreda Code to Official Woreda ID
def woreda_map(all_data_geo, col, title, c):
    woreda_path = r"C:\dev\data\josh-fyp\inputs\ETH_admin_SHP\ETH.shp"
    ethiopia = gpd.read_file(woreda_path)
    IDs = ethiopia[['ADM3', 'geometry']]

    # ID_grouped = (all_data_geo.groupby(by=['ADM3']).mean().reset_index(drop=False))
    data_for_map = all_data_geo[[col, 'ADM3']]
    merged = ethiopia.merge(data_for_map, on='ADM3')
    merged_grouped = (merged.groupby(by='ADM3').mean().reset_index(drop=False))



    merged = ethiopia.set_index('ADM3').join(data_for_map.set_index('ADM3'))
    variable = col

    # Set range for chloropleth
    vmin, vmax = 200, 220
    # a = all_data_geo[col]
    # a = np.ma.masked_where(a == 0, a)
    # cmap = plt.cm.OrRd
    # cmap.set_bad(color='black')

    fig, ax = plt.subplots(1, figsize=(10, 10))
    merged.plot(column=variable, cmap='Wistia', linewidth=0.8, ax=ax, edgecolor='0.8')
    no_data = merged[merged[col] == np.nan]

    # Deets
    # Remove the axis
    ax.axis('off')

    # Add a title
    ax.set_title('Distribution of XYZ', fontdict={'fontsize': '25', 'fontweight':'3'})
    # Annotation for data source
    ax.annotate('Source: Pulled out of my , 2020', xy=(0.1, 0.08), xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')

    # color bar as legend
    sm = plt.cm.ScalarMappable(cmap='Wistia', norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm._A = []
    cbar = fig.colorbar(sm)

    # fig.savefig('map_export.png', dpi=300)

cmaps['Perceptually Uniform Sequential'] = [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis']

cmaps['Sequential'] = [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

def map_cmap(df, col, save_1):
    plt.figure()
    df.plot(column=col, legend=True, scheme='quantiles', missing_kwds={'color': 'lightgrey'}, cmap='Reds')
    plt.title('Average Prevalence Mapping of {} by Woreda'.format(col))
    if save_1 == 1:
        plt.savefig(r"C:\dev\data\josh-fyp\outputs\National_Mapping\{}_woreda_mapping".format(col))


def stats(clim):
    temp = clim[[('tavg', 'jan'), ('tavg', 'feb'), ('tavg', 'mar'), ('tavg', 'apr'), ('tavg', 'mai'), ('tavg', 'jun'), ('tavg', 'jul'), ('tavg', 'aug'), ('tavg', 'sep'), ('tavg', 'oct'), ('tavg', 'nov'), ('tavg', 'dec'), ('tavg', 'djf'), ('tavg', 'mam'), ('tavg', 'jja'), ('tavg', 'son'), ('tavg', 'ann')]]
    prec = clim[[('prec', 'jan'), ('prec', 'feb'), ('prec', 'mar'), ('prec', 'apr'), ('prec', 'mai'), ('prec', 'jun'), ('prec', 'jul'), ('prec', 'aug'), ('prec', 'sep'), ('prec', 'oct'), ('prec', 'nov'), ('prec', 'dec'), ('prec', 'djf'), ('prec', 'mam'), ('prec', 'jja'), ('prec', 'son'), ('prec', 'ann'
    temp_max = clim['temp'].max()
    temp_min = clim['temp'].min()
    temp_diff = abs(clim['temp'].diff().max())

    prec_max = clim['prec'].max()
    prec_min = clim['prec'].min()
    temp_diff = abs(clim['prec'].diff().max())


                                                                                                                                                                                                                                                                                         )]]

