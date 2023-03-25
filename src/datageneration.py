import pandas as pd
import numpy as np

rng = np.random.default_rng(12345)

rints = rng.integers(low=100_000, high=999_999, size=200_000)

bat = list(set(rints))

sites = rng.integers(low=100_000, high=250_000, size=len(bat))

batiments_df = pd.DataFrame({
    'identifiant_site' : sites,
    'identifiant_batiment': bat,
})

sites_uniques = list(set(sites))

communes = pd.read_csv(
    './data/laposte_hexasmal.csv', 
    encoding='utf-8', 
    sep=';', 
    dtype={'Code_commune_INSEE':str, 'Code_postal':str},
    usecols={'Code_commune_INSEE', 'Nom_commune', 'Code_postal'}
)

communes = communes.drop_duplicates(['Code_commune_INSEE'])

code_insee = rng.choice(communes['Code_commune_INSEE'], len(sites_uniques))
numero = rng.integers(low=1, high=145, size=len(sites_uniques))
rue = rng.choice(['rue','avenue','boulevard','place','allee','mail'], len(sites_uniques))
rue_comp = rng.choice(['des fleurs',
                  'de la paix',
                  'du marechal juin',
                  'du manque d\'inspiration',
                  'de l\'ennui profond',
                  'des rosiers',
                  'du chat qui peche',
                  'des oliviers',
                  'de Paris',
                  'des capucins'], len(sites_uniques))


sites_df = pd.DataFrame({
    'identifiant_site' : sites_uniques,
    'code_insee': code_insee,
    'numero': numero ,
    'rue': rue,
    'rue_comp': rue_comp
})

sites_df['adresse'] = sites_df['numero'].astype(str) + " " + sites_df['rue'] + " "  +  sites_df['rue_comp']
sites_df = sites_df.drop(columns=['numero','rue','rue_comp'])

sites_df = sites_df.merge(communes, how='left', left_on='code_insee', right_on='Code_commune_INSEE')



batiments_df = batiments_df.merge(sites_df, how='left', on='identifiant_site')

splits = 20

index_to_split = len(batiments_df) // splits
start = 0
end = index_to_split
for idx, split in enumerate(range(splits)):
    if idx == splits -1:
        end = len(batiments_df)
    temporary_df = batiments_df.iloc[start:end, :]
    start += index_to_split
    end += index_to_split

    temporary_df.to_excel(f'data/batiments/batiments_{idx:02d}.xlsx', index=False)