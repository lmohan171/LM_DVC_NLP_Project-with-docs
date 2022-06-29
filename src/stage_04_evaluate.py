import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils import read_yaml, save_json
import sklearn.metrics as metrics
import math
import numpy as np
import joblib


STAGE = "EVALUATION" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main(config_path, params_path):
    ## read config files
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts=config['artifacts']

    featurized_data_dir_path=os.path.join(artifacts['ARTIFACTS_DIR'],artifacts['FEATURIZED_DATA'])
    featurized_test_data_path=os.path.join(featurized_data_dir_path,artifacts['FEATURIZED_DATA_TEST'])

    model_dir=artifacts['MODEL_DIR']
    model_dir_path=os.path.join(artifacts['ARTIFACTS_DIR'], model_dir)
    model_name=artifacts['MODEL_NAME']
    model_path=os.path.join(model_dir_path, model_name)

    model=joblib.load(model_path)
    matrix=joblib.load(featurized_test_data_path)

    labels=np.squeeze(matrix[:,1].toarray())
    X=matrix[:,2:]

    prediction=model.predict(X)
    print("predict")

    PRC_jason_path=config['plots']['PRC']
    ROC_jason_path=cofig['plots']['ROC']
    scores_jason_path=config['metrics']['SCORES']

    avg_prec=metrics.average_precision_score(labels, prediction)
    roc_auc=metrics.roc_auc_score(labels, prediction)

    scores={
        avg_prec:"avg_prec",
        roc_auc:"roc_auc"
    }

    save_json(scores_jason_path,scores)

    precision, recall, prc_threshold= metrics.precision_recall_curve(labels, prediction)
    nth_point=math.ceil(len(prc_threshold)/1000)
    prc_points=list(zip(precision, recall, prc_threshold))[::nth_point]

    logging.info(f"no. of prc points:{len(prc_points)}")

    prc_data={'prc':[
        {'precision':p, 'recall':r, 'threshold':t} for p, r, t in prc_points
    ]
    }

    save_json(PRC_jason_path,prc_data)

    #for ROC curve
    fpr, tpr, roc_threshold=metrics.roc_curve(labels, prediction)
    roc_data={
        'roc':[{'fpr':fp, 'tpr':tp, 'threshold':t} for fp, tp, t in zip(fpr, tpr, roc_threshold)]}
    logging.info(f"no. of roc points:{len(list(roc_points))}")


    save_json(ROC_jason_path,roc_data)






if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e