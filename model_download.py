from gt4sd.algorithms.registry import ApplicationsRegistry
algorithm = ApplicationsRegistry.get_application_instance(
  target='CCO',
  sampling_wrapper={'property_goal': {'<qed>': 0.12}},
  algorithm_type='conditional_generation',
  domain='materials',
  algorithm_name='RegressionTransformer',
  algorithm_application='RegressionTransformerMolecules',
  algorithm_version='qed'
)