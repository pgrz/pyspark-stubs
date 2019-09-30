from mypy.test.data import DataDrivenTestCase, DataSuite
from mypy.test.testcheck import TypeCheckSuite


class PySparkCoreSuite(TypeCheckSuite):
    TypeCheckSuite.files = [
        "context.test",
        "ml-classification.test",
        "ml-feature.test",
        "ml-param.test",
        "ml-readable.test",
        "resultiterable.test",
        "udf.test",
    ]
    required_out_section = True
