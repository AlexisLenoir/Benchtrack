from BenchTrack.bench2site import bench2site
import sys 

#---------------------------------------------TEST---------------------------------------------

if __name__ == '__main__':
    #path_infra = "/Users/alexislenoir/python/Benchtrack_perso/infrastructures/PGM"
    path_infra = "/Users/alexislenoir/python/Benchtrack_perso/infrastructures/ConfigFichier"
    file_csv = "output.csv"

    if len(sys.argv) > 1:
        path_infra = sys.argv[1]
        file_csv = sys.argv[2]
        path_output = sys.argv[3]
        bench2site(path_infra, file_csv, path_output)
    else:
        bench2site(path_infra, file_csv)