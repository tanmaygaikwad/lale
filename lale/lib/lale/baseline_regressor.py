# Copyright 2019 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np

import lale.docstrings
import lale.operators


class _BaselineRegressorImpl:
    def __init__(self):
        pass

    def fit(self, X, y):
        self._average_label = np.average(y)
        return self

    def predict(self, X):
        result = np.full((X.shape[0],), self._average_label)
        return result


_hyperparams_schema = {
    "allOf": [
        {
            "description": "This first object lists all constructor arguments with their types, but omits constraints for conditional hyperparameters.",
            "type": "object",
            "relevantToOptimizer": [],
            "additionalProperties": False,
        }
    ]
}

_input_fit_schema = {
    "required": ["X", "y"],
    "type": "object",
    "properties": {
        "X": {
            "description": "Features; the outer array is over samples.",
            "type": "array",
            "items": {"type": "array"},
        },
        "y": {
            "description": "Target values.",
            "type": "array",
            "items": {"type": "number"},
        },
    },
}

_input_predict_schema = {
    "type": "object",
    "properties": {
        "X": {
            "description": "Features; the outer array is over samples.",
            "type": "array",
            "items": {"type": "array", "items": {"laleType": "Any"}},
        }
    },
}

_output_predict_schema = {
    "description": "Predicted values per sample.",
    "type": "array",
    "items": {"type": "number"},
}

_combined_schemas = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Baseline regressor always predicts the average target value.",
    "documentation_url": "https://lale.readthedocs.io/en/latest/modules/lale.lib.lale.baseline_regressor.html",
    "import_from": "lale.lib.lale",
    "type": "object",
    "tags": {"pre": [], "op": ["estimator", "regressor"], "post": []},
    "properties": {
        "hyperparams": _hyperparams_schema,
        "input_fit": _input_fit_schema,
        "input_predict": _input_predict_schema,
        "output_predict": _output_predict_schema,
    },
}


BaselineRegressor = lale.operators.make_operator(
    _BaselineRegressorImpl, _combined_schemas
)

lale.docstrings.set_docstrings(BaselineRegressor)
