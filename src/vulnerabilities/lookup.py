

from pathlib import Path
from typing import List, Optional

from .vulnerability_definitions import VULNERABILITY_DEFINITIONS

STRIDE = [
    "Spoofing", "Tampering", "Repudiation",
    "Information Disclosure", "Denial of Service", "Elevation of Privilege",
]


class VulnerabilityLookup:
    """
    Retorna ameaças e contramedidas para um componente e categoria STRIDE.
    """

    def __init__(self, data_path: Optional[Path] = None):
        self.data_path = data_path
        self._cache: dict = VULNERABILITY_DEFINITIONS

    def get_threats(self, component_type: str, stride_category: str) -> List[str]:
        """Lista de ameaças para o par (tipo de componente, STRIDE)."""
        if component_type in self._cache and stride_category in self._cache[component_type]:
            return self._cache[component_type][stride_category].get("threats", [])
        return self._cache["default"].get(stride_category, {}).get("threats", [])

    def get_countermeasures(self, component_type: str, stride_category: str) -> List[str]:
        """Lista de contramedidas para o par (tipo de componente, STRIDE)."""
        if component_type in self._cache and stride_category in self._cache[component_type]:
            return self._cache[component_type][stride_category].get("countermeasures", [])
        return self._cache["default"].get(stride_category, {}).get("countermeasures", [])
