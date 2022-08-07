# Autogenerated by nbdev

d = { 'settings': { 'allowed_cell_metadata_keys': '',
                'allowed_metadata_keys': '',
                'audience': 'Science/Research',
                'author': 'Marcos Santana',
                'author_email': 'marcosvssantana@gmail.com',
                'black_formatting': 'False',
                'branch': 'master',
                'console_scripts': 'nbdev_build_lib=nbdev.cli:nbdev_build_lib',
                'copyright': 'Marcos Santana',
                'custom_sidebar': 'True',
                'description': 'A collection of tools to train graph neural networks for QSAR tasks',
                'doc_baseurl': '/molgraph/',
                'doc_host': 'https://marcossantanaioc.github.io',
                'doc_path': 'docs',
                'git_url': 'https://github.com/marcossantanaioc/molgraph/tree/master/',
                'host': 'github',
                'keywords': 'cheminformatics, machine learning, deep learning, graph neural networks',
                'language': 'English',
                'lib_name': 'molgraph',
                'lib_path': 'molgraph',
                'license': 'apache2',
                'min_python': '3.6',
                'nbs_path': 'notebooks',
                'readme_nb': 'index.ipynb',
                'recursive': 'False',
                'requirements': 'nbdev fastai matplotlib seaborn tqdm rdkit-pypi',
                'status': '3',
                'title': 'molgraph',
                'tst_flags': '',
                'user': 'marcossantanaioc',
                'version': '0.2'},
  'syms': { 'molgraph..ipynb_checkpoints.all-checkpoint': {},
            'molgraph..ipynb_checkpoints.layers-checkpoint': { 'molgraph..ipynb_checkpoints.layers-checkpoint.MessageGCN': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.layers-checkpoint.html#messagegcn',
                                                               'molgraph..ipynb_checkpoints.layers-checkpoint.MessageGCN.forward': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.layers-checkpoint.html#messagegcn.forward',
                                                               'molgraph..ipynb_checkpoints.layers-checkpoint.UpdateGCN': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.layers-checkpoint.html#updategcn',
                                                               'molgraph..ipynb_checkpoints.layers-checkpoint.UpdateGCN.forward': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.layers-checkpoint.html#updategcn.forward',
                                                               'molgraph..ipynb_checkpoints.layers-checkpoint.feed_forward': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.layers-checkpoint.html#feed_forward'},
            'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint': { 'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.AtomFeaturizer': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#atomfeaturizer',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.AtomFeaturizer.encode': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#atomfeaturizer.encode',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.AtomFeaturizer.get_atomic_num': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#atomfeaturizer.get_atomic_num',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.AtomFeaturizer.get_chiral': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#atomfeaturizer.get_chiral',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.AtomFeaturizer.get_degree': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#atomfeaturizer.get_degree',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.AtomFeaturizer.get_formal_charge': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#atomfeaturizer.get_formal_charge',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.AtomFeaturizer.get_hybridization': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#atomfeaturizer.get_hybridization',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.AtomFeaturizer.get_is_aromatic': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#atomfeaturizer.get_is_aromatic',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.AtomFeaturizer.get_mass': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#atomfeaturizer.get_mass',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.AtomFeaturizer.get_numh': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#atomfeaturizer.get_numh',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.BondFeaturizer': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#bondfeaturizer',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.BondFeaturizer.encode': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#bondfeaturizer.encode',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.BondFeaturizer.get_bondtype': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#bondfeaturizer.get_bondtype',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.BondFeaturizer.get_isconjugated': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#bondfeaturizer.get_isconjugated',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.BondFeaturizer.get_isring': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#bondfeaturizer.get_isring',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.BondFeaturizer.get_stereo': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#bondfeaturizer.get_stereo',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.CHIRAL_DICT': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#chiral_dict',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.ELEMENTS': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#elements',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.HYBRIDIZATION': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#hybridization',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolGraphDataLoader': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#molgraphdataloader',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolGraphDataLoader.dataloders': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#molgraphdataloader.dataloders',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularDataset': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculardataset',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularDataset.copy': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculardataset.copy',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularDataset.x': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculardataset.x',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularDataset.y': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculardataset.y',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraph': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraph',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraph.mol_to_graph': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraph.mol_to_graph',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset.copy': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset.copy',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset.create_dataset': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset.create_dataset',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset.from_csv': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset.from_csv',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset.from_df': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset.from_df',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset.save_dir': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset.save_dir',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset.splits': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset.splits',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset.timestamp': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset.timestamp',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset.train': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset.train',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset.valid': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset.valid',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset.x': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset.x',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.MolecularGraphDataset.y': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#moleculargraphdataset.y',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.TARGET2TYPE': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#target2type',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.TYPE2TARGET': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#type2target',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.convert_smiles': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#convert_smiles',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.encode_onehot': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#encode_onehot',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.molgraph_collate_fn': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#molgraph_collate_fn',
                                                                        'molgraph..ipynb_checkpoints.molgraphdataset-checkpoint.save_df': 'https://marcossantanaioc.github.io/molgraph/.ipynb_checkpoints.molgraphdataset-checkpoint.html#save_df'},
            'molgraph.all': {},
            'molgraph.layers': { 'molgraph.layers.MessageGCN': 'https://marcossantanaioc.github.io/molgraph/layers.html#messagegcn',
                                 'molgraph.layers.MessageGCN.forward': 'https://marcossantanaioc.github.io/molgraph/layers.html#messagegcn.forward',
                                 'molgraph.layers.UpdateGCN': 'https://marcossantanaioc.github.io/molgraph/layers.html#updategcn',
                                 'molgraph.layers.UpdateGCN.forward': 'https://marcossantanaioc.github.io/molgraph/layers.html#updategcn.forward',
                                 'molgraph.layers.feed_forward': 'https://marcossantanaioc.github.io/molgraph/layers.html#feed_forward'},
            'molgraph.models.gcnn': { 'molgraph.models.gcnn.GCNMPNmodel': 'https://marcossantanaioc.github.io/molgraph/models.gcnn.html#gcnmpnmodel',
                                      'molgraph.models.gcnn.GCNMPNmodel.forward': 'https://marcossantanaioc.github.io/molgraph/models.gcnn.html#gcnmpnmodel.forward'},
            'molgraph.molgraphdataset': { 'molgraph.molgraphdataset.AtomFeaturizer': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#atomfeaturizer',
                                          'molgraph.molgraphdataset.AtomFeaturizer.encode': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#atomfeaturizer.encode',
                                          'molgraph.molgraphdataset.AtomFeaturizer.get_atomic_num': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#atomfeaturizer.get_atomic_num',
                                          'molgraph.molgraphdataset.AtomFeaturizer.get_chiral': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#atomfeaturizer.get_chiral',
                                          'molgraph.molgraphdataset.AtomFeaturizer.get_degree': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#atomfeaturizer.get_degree',
                                          'molgraph.molgraphdataset.AtomFeaturizer.get_formal_charge': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#atomfeaturizer.get_formal_charge',
                                          'molgraph.molgraphdataset.AtomFeaturizer.get_hybridization': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#atomfeaturizer.get_hybridization',
                                          'molgraph.molgraphdataset.AtomFeaturizer.get_is_aromatic': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#atomfeaturizer.get_is_aromatic',
                                          'molgraph.molgraphdataset.AtomFeaturizer.get_mass': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#atomfeaturizer.get_mass',
                                          'molgraph.molgraphdataset.AtomFeaturizer.get_numh': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#atomfeaturizer.get_numh',
                                          'molgraph.molgraphdataset.BondFeaturizer': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#bondfeaturizer',
                                          'molgraph.molgraphdataset.BondFeaturizer.encode': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#bondfeaturizer.encode',
                                          'molgraph.molgraphdataset.BondFeaturizer.get_bondtype': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#bondfeaturizer.get_bondtype',
                                          'molgraph.molgraphdataset.BondFeaturizer.get_isconjugated': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#bondfeaturizer.get_isconjugated',
                                          'molgraph.molgraphdataset.BondFeaturizer.get_isring': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#bondfeaturizer.get_isring',
                                          'molgraph.molgraphdataset.BondFeaturizer.get_stereo': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#bondfeaturizer.get_stereo',
                                          'molgraph.molgraphdataset.CHIRAL_DICT': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#chiral_dict',
                                          'molgraph.molgraphdataset.ELEMENTS': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#elements',
                                          'molgraph.molgraphdataset.HYBRIDIZATION': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#hybridization',
                                          'molgraph.molgraphdataset.MolGraphDataLoader': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#molgraphdataloader',
                                          'molgraph.molgraphdataset.MolGraphDataLoader.dataloaders': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#molgraphdataloader.dataloaders',
                                          'molgraph.molgraphdataset.MolecularDataset': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculardataset',
                                          'molgraph.molgraphdataset.MolecularDataset.copy': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculardataset.copy',
                                          'molgraph.molgraphdataset.MolecularDataset.x': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculardataset.x',
                                          'molgraph.molgraphdataset.MolecularDataset.y': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculardataset.y',
                                          'molgraph.molgraphdataset.MolecularGraph': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraph',
                                          'molgraph.molgraphdataset.MolecularGraph.mol_to_graph': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraph.mol_to_graph',
                                          'molgraph.molgraphdataset.MolecularGraphDataset': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset',
                                          'molgraph.molgraphdataset.MolecularGraphDataset.copy': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset.copy',
                                          'molgraph.molgraphdataset.MolecularGraphDataset.create_dataset': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset.create_dataset',
                                          'molgraph.molgraphdataset.MolecularGraphDataset.from_csv': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset.from_csv',
                                          'molgraph.molgraphdataset.MolecularGraphDataset.from_df': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset.from_df',
                                          'molgraph.molgraphdataset.MolecularGraphDataset.save_dir': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset.save_dir',
                                          'molgraph.molgraphdataset.MolecularGraphDataset.splits': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset.splits',
                                          'molgraph.molgraphdataset.MolecularGraphDataset.timestamp': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset.timestamp',
                                          'molgraph.molgraphdataset.MolecularGraphDataset.train': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset.train',
                                          'molgraph.molgraphdataset.MolecularGraphDataset.valid': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset.valid',
                                          'molgraph.molgraphdataset.MolecularGraphDataset.x': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset.x',
                                          'molgraph.molgraphdataset.MolecularGraphDataset.y': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#moleculargraphdataset.y',
                                          'molgraph.molgraphdataset.TARGET2TYPE': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#target2type',
                                          'molgraph.molgraphdataset.TYPE2TARGET': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#type2target',
                                          'molgraph.molgraphdataset.convert_smiles': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#convert_smiles',
                                          'molgraph.molgraphdataset.encode_onehot': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#encode_onehot',
                                          'molgraph.molgraphdataset.molgraph_collate_fn': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#molgraph_collate_fn',
                                          'molgraph.molgraphdataset.save_df': 'https://marcossantanaioc.github.io/molgraph/molgraphdataset.html#save_df'}}}