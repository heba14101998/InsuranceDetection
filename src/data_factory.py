
from base import Base
import numpy as np
import pandas as pd
import joblib
from pathlib import Path
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
class DataFactory(Base):
    
    def __init__(self):
        super().__init__()
        self.train_data_path = self.config['paths']['train_path']
        self.cat_cols = self.config['data']['categorical_cols']
        self.num_cols = self.config['data']['numercal_cols']
        self.target_col = self.config['data']['target_col']
        self.transform_data_path = self.config['paths']['transformed_data_path']
        self.preprocessor_path = Path(self.config['paths']['preprocessor_path'])

        self.preprocessor = self._make_preprocessor()
        self.transformed_data = None

    def data_clean(self, data):
        # Drop irrelevant
        data.drop(columns=['id'], axis=1, inplace=True)
        
        # Handle inconcistent data
        data['AnnualPremium'] = data['AnnualPremium'].str.replace("£", "").str.replace(",", "").astype(float)
        
        mapping = {'< 1 Year': 0.5,'1-2 years': 1.5,'> 2 years': 2.5}
        data['VehicleAge'] = data['VehicleAge'].map(mapping)
        self.logger.info(f"VehicleAge: {data['VehicleAge'].unique()}")

        # Impute Missing
        imputer = SimpleImputer(missing_values=np.nan, strategy='median')
        data[self.num_cols] = imputer.fit_transform(data[self.num_cols])

        imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
        data[self.cat_cols]= imputer.fit_transform(data[self.cat_cols])
        self.logger.info(f"Missing Data Imputed")

        # Remove outliers 
        self.logger.info(f"Data shape before removing outliers: {data.shape}")
        Q1 = data['AnnualPremium'].quantile(0.25)
        Q3 = data['AnnualPremium'].quantile(0.75)
        IQR = Q3 - Q1
        upper_bound = Q3 + 1.5 * IQR
        lower_bound = Q1 - 1.5 * IQR
        data = data[(data['AnnualPremium'] <= upper_bound) & (data['AnnualPremium'] >= lower_bound)]
        self.logger.info(f"Data shape after removing outliers: {data.shape}")

        return data

    def _make_preprocessor(self):
        # nummerical --> scaling 
        # categorical --> encoding
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), self.num_cols ),
                ('cat', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1) , self.cat_cols)  # LabelEncoder
            ]
        )
        return preprocessor
        
    def fit_preprocessor(self, data):
        data = data[self.num_cols + self.cat_cols]
        self.preprocessor.fit(data)
        self.logger.info(f"Preprocessor fitted")
        return self.preprocessor

    def transform_data(self, data):

        transformed_data_np = self.preprocessor.transform(data)
        columns = self.preprocessor.get_feature_names_out()
        self.transformed_data = pd.DataFrame(transformed_data_np, columns=columns)
        self.logger.info(f"Transformed data shape: {self.transformed_data.shape}")

        return self.transformed_data

    def save_transformed_data(self):
        self.transformed_data.to_csv(self.transform_data_path, index=False)
        self.logger.info(f"Transformed data saved to {self.transform_data_path}")

    def save_preprocessor(self):
        joblib.dump(self.preprocessor, self.preprocessor_path)
        self.logger.info(f"Preprocessor saved to {self.preprocessor_path}")

"""
if __name__ =='__main__':
    import pandas as pd

    #  1. Read Data from CSV
    data_path = "data\\raw\\train.csv"
    df = pd.read_csv(data_path)
    data_factory = DataFactory()

    # 2. Data Cleaning
    clean_df =data_factory.data_clean(data=df)  

    # 3. Data preprocessing
    _ = data_factory.fit_preprocessor(data=clean_df)

    transform_data = data_factory.transform_data(data=clean_df)

    data_factory.save_transformed_data()
    data_factory.save_preprocessor()
"""

        
