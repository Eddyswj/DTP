import numpy as np

def run(Averagetemp, Airquality, Pesticides, Annualprecipitation, crops):

    X = np.array([Annualprecipitation, Averagetemp, Pesticides, Airquality])

    Crops = crops

    #fixed calculated variables from model
    betas = {'Maize': np.array([[ 36598.78116881],[-876.91315758],[-14098.44434371],[-57.05564375],[-951.82570797]]),
        'Potatoes': np.array([[200480.24652981],[-23812.37291411],[-14318.78945994],[21607.93023378],[-20046.87116057]]),
        'Rice, paddy': np.array([[40736.1963531],[-3294.47541661],[-3690.16797772],[4781.1473144 ],[-3649.30351158]]),
        'Sorghum': np.array([[18703.93679228],[-659.56936905],[-4467.62863625],[3780.07895115],[-2315.24767696]]),
        'Soybeans': np.array([[16720.58367581],[-242.05036426],[-1453.01620323],[550.07575197],[-2869.06383225]]),
        'Wheat': np.array([[30262.79313027],[-1635.33821576],[-7353.30510908],[2689.4874744 ],[2335.66760226]]),
        'Cassava': np.array([[150881.11296269],[4699.05487448],[-21765.04799557],[20086.50662626],[1389.87413779]]),
        'Sweet potatoes': np.array([[119098.911436  ],[-20361.60443617],[-13686.44396246],[16970.9104816 ],[-11208.13340487]]),
        'Plantains and others': np.array([[103735.32641901],[-22264.95722228],[-13963.87740904],[16118.29897833],[1701.45294564]]),
        'Yams': np.array([[114561.32832873],[4699.05487448],[-21765.04799557],[20086.50662626],[1389.87413779]])}

    return get_best_crop(X, betas, Crops)

def normalize_z(array, 
            columns_means=None, 
            columns_stds=None):

    if columns_means is None:
        columns_means = np.mean(array, axis=0)
    if columns_stds is None:
        columns_stds = np.std(array, axis=0)

    out = np.divide(array - columns_means,columns_stds)


    return out, columns_means, columns_stds

def prepare_feature(np_feature):


    np_feature = np_feature.reshape(1,-1)

    no_rows = np_feature.shape[0]
    return np.concatenate((np.ones((no_rows,1)), np_feature), axis = 1)

def calc_linreg(X: np.ndarray, beta: np.ndarray):

    return np.matmul(X, beta)

def predict_linreg(array_feature, beta, 
                means=None, 
                stds=None):

    normalized, _, _ = normalize_z(array_feature, means, stds)
    X = prepare_feature(normalized)
    return calc_linreg(X, beta)

def get_best_crop(X, betas, Crops): #returns name of best crop to plant

    crop_ys = {}
    for crop in Crops:
        crop_ys[crop] = predict_linreg(X, betas[crop])

    max_yield = 0
    best_crop = []
    for i, v in crop_ys.items():
        if v > max_yield:
            best_crop = i
            max_yield = [v]
        elif v == max_yield:
            best_crop.append(i) 


    return best_crop