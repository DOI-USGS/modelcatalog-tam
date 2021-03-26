from BasicProfileSchema import BasicProfile


from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum


class AdvancedProfile(BaseModel):
    """Advanced metadata profile
    Fields
    ------
    requirements = Optional[str]
        Software and/or hardware requirements needed to run the model and replicate any published results.
    dependencies = Optional[str]
        All data dependencies needed to run the model and replicate any published results.
    installation_info = Optional[str]
        Information on how to install the model so that it can be run (e.g., compilation and/or execution instructions).
    assumptions = Optional[str]
        Key assumptions made that define the dynamics of the model.
    model_structure = Optional[str]
        Provide a flow diagram of the model
    equations_rules = Optional[str]
        What are the equations and rules of the model?
    temporal_info = Optional[str]
        Temporal resolution, time stepping, and units.
    spatial_info = Optional[str]
        Spatial dimensionality, resolution, extent, grid type if relevant.
    limitations = Optional[str]
        Limitations, domain ranges: What is this model specifically NOT intended to do.
    input_parameters = Optional[str]
        Key input parameters and their values and domain ranges and units (minimum input requirements for model operation and default values, where appropriate).
    output_variables = Optional[str]
        Key output parameters and their values and domain ranges and units.
    sample_input_output = Optional[str]
        Provide links to sample input and output files, including run script, such as a cookbook or benchmark.
    initial_conditions: Optional[str]
        For example, starting points like the initial state of variables i.e. wind, temperatures, pressure, and moisture.
    functions: Optional[str]
        Forcing functions that affect the dynamics of the model.
    example: Optional[str]
        Sample runs that illustrate the dynamics of the model.
    calibration: Optional[str]
        Provide data used for calibration and evaluation of the model, if data are public.
    evalution_uncertainty_sensitivity: Optional[str]
        List of publications or links on evaluation, uncertainty, sensitivity analyses for your model.
    benchmarks: Optional[str]
        Describe or provide benchmarks for validation of your model.
    usage_activity: Optional[str]
        Metrics that can be obtained from repository API, such as repo commits.
    methods: Optional[str]
        Machine learning or statistical model (random forest, neural network
    tasks: Optional[str]
        Image classification, segmentation, etc.
    applications: Optional[str]
        Tracking rainfall thresholds, predicting population, etc.


    Example
    -------
    >>> BasicProfile(item_type="model",
    ...              name="COAWST",
    ...              description="sample description")
    BasicProfile(item_type=<ModelTypeEnum.model: 'model'>, name='COAWST', description='sample description', organization=True, external_organization_name=None, release_date=None, last_update=None, subtitle=None, author=None, contact=None, version=None, how_to_cite=None, usgs_missionarea=None, identifier=None, programming_language=None, license='CC0', resources=None, references=None, science_keywords=None, type_keywords=None, other_keywords=None, image=None, related_catalog_item=None)
    """

    _version: str = "v1.0.0"

    requirements = Optional[str]
    dependencies = Optional[str]
    installation_info = Optional[str]
    assumptions = Optional[str]
    model_structure = Optional[str]
    equations_rules = Optional[str]
    temporal_info = Optional[str]
    spatial_info = Optional[str]
    limitations = Optional[str]
    input_parameters = Optional[str]
    output_variables = Optional[str]
    sample_input_output = Optional[str]
    initial_conditions: Optional[str]
    functions: Optional[str]
    example: Optional[str]
    calibration: Optional[str]
    evalution_uncertainty_sensitivity: Optional[str]
    benchmarks: Optional[str]
    usage_activity: Optional[str]
    methods: Optional[List[str]]
    tasks: Optional[List[str]]
    applications: Optional[List[str]]
