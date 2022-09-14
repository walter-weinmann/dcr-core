# pylint: disable=unused-argument
"""Testing Class LineTypeToc."""
import pytest

import dcr_core.cls_line_type_header_footer as lt_hf
import dcr_core.cls_line_type_toc as lt_toc
import dcr_core.cls_text_parser as parser
from dcr_core import core_glob

# -----------------------------------------------------------------------------
# Constants & Globals.
# -----------------------------------------------------------------------------
# @pytest.mark.issue


# -----------------------------------------------------------------------------
# Test Cases Line Type Toc - Coverage.
# -----------------------------------------------------------------------------
def test(fxtr_rmdir_opt, fxtr_setup_empty_inbox):
    """Test Cases Line Type Toc - Coverage."""
    # -------------------------------------------------------------------------
    try:
        del core_glob.text_parser
    except (AttributeError, NameError):
        pass

    with pytest.raises(SystemExit) as expt:
        lt_toc.LineTypeToc()

    assert expt.type == SystemExit, "Instance of TextParser is missing"
    assert expt.value.code == 1, "Instance of TextParser is missing"

    core_glob.text_parser = parser.TextParser()

    # -------------------------------------------------------------------------
    try:
        del core_glob.line_type_header_footer
    except (AttributeError, NameError):
        pass

    with pytest.raises(SystemExit) as expt:
        lt_toc.LineTypeToc()

    assert expt.type == SystemExit, "Instance of LineTypeHeaderFooter is missing"
    assert expt.value.code == 1, "Instance of LineTypeHeaderFooter is missing"

    core_glob.line_type_header_footer = lt_hf.LineTypeHeaderFooter()

    # -------------------------------------------------------------------------
    instance = lt_toc.LineTypeToc()

    instance.exists()
