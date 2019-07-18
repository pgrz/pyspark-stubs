# Stubs for pyspark.ml.evaluation (Python 3.5)
#

from typing import Any, Dict, Optional
from pyspark.ml.wrapper import JavaParams
from pyspark.ml.param import Param, Params
from pyspark.ml.param.shared import HasFeaturesCol, HasLabelCol, HasPredictionCol, HasRawPredictionCol, HasWeightCol
from pyspark.ml.util import JavaMLReadable, JavaMLWritable

ParamMap = Dict[Param, Any]

class Evaluator(Params):
    __metaclass__ = ...  # type: Any
    def evaluate(self, dataset, params: Optional[ParamMap] = ...) -> float: ...
    def isLargerBetter(self) -> bool: ...

class JavaEvaluator(JavaParams, Evaluator):
    __metaclass__ = ...  # type: Any
    def isLargerBetter(self) -> bool: ...

class BinaryClassificationEvaluator(JavaEvaluator, HasLabelCol, HasRawPredictionCol, HasWeightCol, JavaMLReadable, JavaMLWritable):
    metricName = ...  # type: Param
    def __init__(self, rawPredictionCol: str = ..., labelCol: str = ..., metricName: str = ..., weightCol: Optional[str] = ...) -> None: ...
    def setMetricName(self, value: str) -> BinaryClassificationEvaluator: ...
    def getMetricName(self) -> str: ...
    def setParams(self, rawPredictionCol: str = ..., labelCol: str = ..., metricName: str = ..., weightCol: Optional[str] = ...) -> BinaryClassificationEvaluator: ...

class RegressionEvaluator(JavaEvaluator, HasLabelCol, HasPredictionCol, HasWeightCol, JavaMLReadable, JavaMLWritable):
    metricName = ...  # type: Param
    def __init__(self, predictionCol: str = ..., labelCol: str = ..., metricName: str = ..., weightCol: Optional[str] = ...) -> None: ...
    def setMetricName(self, value: str) -> RegressionEvaluator: ...
    def getMetricName(self) -> str: ...
    def setParams(self, predictionCol: str = ..., labelCol: str = ..., metricName: str = ..., weightCol: Optional[str] = ...) -> RegressionEvaluator: ...

class MulticlassClassificationEvaluator(JavaEvaluator, HasLabelCol, HasPredictionCol, JavaMLReadable, JavaMLWritable):
    metricName = ...  # type: Param
    def __init__(self, predictionCol: str = ..., labelCol: str = ..., metricName: str = ...) -> None: ...
    def setMetricName(self, value: str) -> MulticlassClassificationEvaluator: ...
    def getMetricName(self) -> str: ...
    def setParams(self, predictionCol: str = ..., labelCol: str = ..., metricName: str = ...) -> MulticlassClassificationEvaluator: ...

class ClusteringEvaluator(JavaEvaluator, HasPredictionCol, HasFeaturesCol, JavaMLReadable, JavaMLWritable):
    metricName = ...  # type: Param
    distanceMeasure = ...  # type: Param
    def __init__(self, predictionCol: str = ..., featuresCol: str = ..., metricName: str = ..., distanceMeasure: str = ...) -> None: ...
    def setMetricName(self, value: str) -> ClusteringEvaluator: ...
    def getMetricName(self) -> str: ...
    def setParams(self, predictionCol: str = ..., featuresCol: str = ..., metricName: str = ..., distanceMeasure: str = ...) -> MulticlassClassificationEvaluator: ...
    def setDistanceMeasure(self, value: str) -> MulticlassClassificationEvaluator: ...
    def getDistanceMeasure(self) -> str: ...
