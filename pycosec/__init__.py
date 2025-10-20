"""
pycosec package


Expose the main client class at package level for convenience.
"""


from .biometric import COSECBiometric


__all__ = ["COSECBiometric"]
__version__ = "0.1.0"