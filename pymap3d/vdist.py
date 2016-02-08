"""
A thin shell vdist() around GeoPy Vincenty distance algorithm for those who might be looking
for the vdist() companion to the Michael Kleder vreckon()
"""

from geopy.distance import vincenty

def vdist(lat1,lon1,lat2,lon2):
    return vincenty((lat1,lon1),(lat2,lon2)).meters

if __name__ == '__main__': #pragma: no cover
    from argparse import ArgumentParser
    p = ArgumentParser(description='vdist distance between WGS-84 coordinates')
    p.add_argument('lat1',help='latitude1 WGS-84 [degrees]',type=float)
    p.add_argument('lon1',help='longitude1 WGS-84 [degrees]',type=float)
    p.add_argument('lat2',help='latitude2 WGS-84 [degrees]',type=float)
    p.add_argument('lon2',help='longitude2 WGS-84 [degrees]',type=float)
    p = p.parse_args()

    dist_m = vdist(p.lat1, p.lon1, p.lat2, p.lon2)
    print('distance between WGS-84 points = {} m'.format(dist_m))
