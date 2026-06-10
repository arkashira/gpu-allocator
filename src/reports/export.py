"""Report export functionality for axentx GPU Allocator.

Supports CSV, JSON, XLSX, and PDF output.  The :class:`ReportExporter`
accepts a list of GPU-usage records (as produced by the analytics
pipeline) plus a time range, and writes a report to disk or returns
bytes for streaming.
"""

from __future__ import annotations

import csv
import io
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Union

from .exceptions import ExportError, UnsupportedFormatError
from .formatters import aggregate_summary, flatten_gpu_records

logger = logging.getLogger(__name__)

SUPPORTED_FORMATS = ("csv", "json", "xlsx", "pdf")


# --------------------------------------------------
