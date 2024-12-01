import numpy as np

def run(Temperature, Pollution, Pesticides, Precipitation, crops):

    X = np.array([Pesticides,Temperature,Pollution,Precipitation])

    #fixed calculated variables from model
    betas = {'Potato': np.array([[18.14467658],[4.05261727],[-2.64548464],[-1.61457113],[-2.60145514]]), 
             'Soybean': np.array([[1.58583017],[0.26298947],[-0.16083612],[-0.17840645],[-0.11213534]]),
             'Wheat': np.array([[2.87015384],[0.53180323],[-0.76048294],[-0.14527727],[-0.1687206 ]]),
             'Rice': np.array([[3.44034162],[0.60632698],[-0.64445607],[-0.13890819],[-0.18263675]]),
             'Corn': np.array([[3.66508388],[1.12566249],[-1.52735066],[-0.11911551],[-0.49961753]]),
             'Cassava': np.array([[10.6108354 ],[0.76750492],[1.44578981],[-0.95765497],[0.72488331]])}
    
    return get_best_crop(X, betas, crops)


def normalize_z(array, 
                columns_means=None, 
                columns_stds=None):
    
    if columns_means is None:
        columns_means = np.mean(array, axis=0)
    if columns_stds is None:
        columns_stds = np.std(array, axis=0)
    
    out = np.divide(array - columns_means,columns_stds)
    
    return out, columns_means, columns_stds


    return out, columns_means, columns_stds

def prepare_feature(np_feature):
    
    np_feature = np_feature.reshape(1,-1)

    no_rows = np_feature.shape[0]
    return np.concatenate((np.ones((no_rows,1)), np_feature), axis = 1)


def calc_linreg(X: np.ndarray, beta: np.ndarray):
    
    return np.matmul(X, beta)


def predict_linreg_z(array_feature, beta, 
                   means=None, 
                   stds=None):
    
    normalized, _, _ = normalize_z(array_feature, means, stds)
    X = prepare_feature(normalized)
    return calc_linreg(X, beta)

def get_best_crop(X, betas, Crops): #returns name of best crop to plant

    crop_ys = {}
    for crop in Crops:
        crop_ys[crop] = predict_linreg_z(X, betas[crop])

    max_yield = 0
    best_crop = []
    for i, v in crop_ys.items():
        if v > max_yield:
            best_crop = i
            max_yield = [v]
        elif v == max_yield:
            best_crop.append(i) 
    
    return best_crop

