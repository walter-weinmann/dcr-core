# Copyright (c) 2022 Konnexions GmbH. All rights reserved. Use of this
# source code is governed by the Konnexions Public License (KX-PL)
# Version 2020.05, that can be found in the LICENSE file.

"""Managing the application configuration parameters.

Typical usage example:

    my_instance = Setup()
"""
from __future__ import annotations

import configparser
import os
from typing import ClassVar

from dcr_core import core_glob
from dcr_core import core_utils


# pylint: disable=too-many-instance-attributes
class Setup:
    """Managing the application configuration parameters."""

    # ------------------------------------------------------------------
    # Class variables.
    # ------------------------------------------------------------------
    _CONFIG_PARAM_NO: ClassVar[int] = 117

    _DCR_CFG_DELETE_AUXILIARY_FILES: ClassVar[str] = "delete_auxiliary_files"
    _DCR_CFG_DIRECTORY_INBOX: ClassVar[str] = "directory_inbox"
    _DCR_CFG_FILE: ClassVar[str] = "setup.cfg"
    _DCR_CFG_JSON_INCL_CONFIG: ClassVar[str] = "json_incl_config"
    _DCR_CFG_JSON_INCL_FONTS: ClassVar[str] = "json_incl_fonts"
    _DCR_CFG_JSON_INCL_HEADING: ClassVar[str] = "json_incl_heading"
    _DCR_CFG_JSON_INCL_LIST_BULLET: ClassVar[str] = "json_incl_list_bullet"
    _DCR_CFG_JSON_INCL_LIST_NUMBER: ClassVar[str] = "json_incl_list_number"
    _DCR_CFG_JSON_INCL_PARAMS: ClassVar[str] = "json_incl_params"
    _DCR_CFG_JSON_INDENT: ClassVar[str] = "json_indent"
    _DCR_CFG_JSON_SORT_KEYS: ClassVar[str] = "json_sort_keys"
    _DCR_CFG_LT_FOOTER_MAX_DISTANCE: ClassVar[str] = "lt_footer_max_distance"
    _DCR_CFG_LT_FOOTER_MAX_LINES: ClassVar[str] = "lt_footer_max_lines"
    _DCR_CFG_LT_FOOTER_REQUIRED: ClassVar[str] = "lt_footer_required"
    _DCR_CFG_LT_HEADER_MAX_DISTANCE: ClassVar[str] = "lt_header_max_distance"
    _DCR_CFG_LT_HEADER_MAX_LINES: ClassVar[str] = "lt_header_max_lines"
    _DCR_CFG_LT_HEADER_REQUIRED: ClassVar[str] = "lt_header_required"
    _DCR_CFG_LT_HEADING_FILE_INCL_NO_CTX: ClassVar[str] = "lt_heading_file_incl_no_ctx"
    _DCR_CFG_LT_HEADING_FILE_INCL_REGEXP: ClassVar[str] = "lt_heading_file_incl_regexp"
    _DCR_CFG_LT_HEADING_MAX_LEVEL: ClassVar[str] = "lt_heading_max_level"
    _DCR_CFG_LT_HEADING_MIN_PAGES: ClassVar[str] = "lt_heading_min_pages"
    _DCR_CFG_LT_HEADING_REQUIRED: ClassVar[str] = "lt_heading_required"
    _DCR_CFG_LT_HEADING_RULE_FILE: ClassVar[str] = "lt_heading_rule_file"
    _DCR_CFG_LT_HEADING_TOLERANCE_LLX: ClassVar[str] = "lt_heading_tolerance_llx"
    _DCR_CFG_LT_LIST_BULLET_MIN_ENTRIES: ClassVar[str] = "lt_list_bullet_min_entries"
    _DCR_CFG_LT_LIST_BULLET_REQUIRED: ClassVar[str] = "lt_list_bullet_required"
    _DCR_CFG_LT_LIST_BULLET_RULE_FILE: ClassVar[str] = "lt_list_bullet_rule_file"
    _DCR_CFG_LT_LIST_BULLET_TOLERANCE_LLX: ClassVar[str] = "lt_list_bullet_tolerance_llx"
    _DCR_CFG_LT_LIST_NUMBER_FILE_INCL_REGEXP: ClassVar[str] = "lt_list_number_file_incl_regexp"
    _DCR_CFG_LT_LIST_NUMBER_MIN_ENTRIES: ClassVar[str] = "lt_list_number_min_entries"
    _DCR_CFG_LT_LIST_NUMBER_REQUIRED: ClassVar[str] = "lt_list_number_required"
    _DCR_CFG_LT_LIST_NUMBER_RULE_FILE: ClassVar[str] = "lt_list_number_rule_file"
    _DCR_CFG_LT_LIST_NUMBER_TOLERANCE_LLX: ClassVar[str] = "lt_list_number_tolerance_llx"
    _DCR_CFG_LT_TOC_LAST_PAGE: ClassVar[str] = "lt_toc_last_page"
    _DCR_CFG_LT_TOC_MIN_ENTRIES: ClassVar[str] = "lt_toc_min_entries"
    _DCR_CFG_LT_TOC_REQUIRED: ClassVar[str] = "lt_toc_required"
    _DCR_CFG_PDF2IMAGE_TYPE: ClassVar[str] = "pdf2image_type"
    _DCR_CFG_SECTION_CORE: ClassVar[str] = "dcr_core"
    _DCR_CFG_SECTION_CORE_ENV_TEST: ClassVar[str] = "dcr_core.env.test"
    _DCR_CFG_SECTION_CORE_SPACY: ClassVar[str] = "dcr_core.spacy"

    _DCR_CFG_SPACY_IGNORE_BRACKET: ClassVar[str] = "spacy_ignore_bracket"
    _DCR_CFG_SPACY_IGNORE_LEFT_PUNCT: ClassVar[str] = "spacy_ignore_left_punct"
    _DCR_CFG_SPACY_IGNORE_LINE_TYPE_FOOTER: ClassVar[str] = "spacy_ignore_line_type_footer"
    _DCR_CFG_SPACY_IGNORE_LINE_TYPE_HEADER: ClassVar[str] = "spacy_ignore_line_type_header"
    _DCR_CFG_SPACY_IGNORE_LINE_TYPE_HEADING: ClassVar[str] = "spacy_ignore_line_type_heading"
    _DCR_CFG_SPACY_IGNORE_LINE_TYPE_LIST_BULLET: ClassVar[str] = "spacy_ignore_line_type_list_bullet"
    _DCR_CFG_SPACY_IGNORE_LINE_TYPE_LIST_NUMBER: ClassVar[str] = "spacy_ignore_line_type_list_number"
    _DCR_CFG_SPACY_IGNORE_LINE_TYPE_TABLE: ClassVar[str] = "spacy_ignore_line_type_table"
    _DCR_CFG_SPACY_IGNORE_LINE_TYPE_TOC: ClassVar[str] = "spacy_ignore_line_type_toc"
    _DCR_CFG_SPACY_IGNORE_PUNCT: ClassVar[str] = "spacy_ignore_punct"
    _DCR_CFG_SPACY_IGNORE_QUOTE: ClassVar[str] = "spacy_ignore_quote"
    _DCR_CFG_SPACY_IGNORE_RIGHT_PUNCT: ClassVar[str] = "spacy_ignore_right_punct"
    _DCR_CFG_SPACY_IGNORE_SPACE: ClassVar[str] = "spacy_ignore_space"
    _DCR_CFG_SPACY_IGNORE_STOP: ClassVar[str] = "spacy_ignore_stop"

    _DCR_CFG_SPACY_TKN_ATTR_CLUSTER: ClassVar[str] = "spacy_tkn_attr_cluster"
    _DCR_CFG_SPACY_TKN_ATTR_DEP_: ClassVar[str] = "spacy_tkn_attr_dep_"
    _DCR_CFG_SPACY_TKN_ATTR_DOC: ClassVar[str] = "spacy_tkn_attr_doc"
    _DCR_CFG_SPACY_TKN_ATTR_ENT_IOB_: ClassVar[str] = "spacy_tkn_attr_ent_iob_"
    _DCR_CFG_SPACY_TKN_ATTR_ENT_KB_ID_: ClassVar[str] = "spacy_tkn_attr_ent_kb_id_"
    _DCR_CFG_SPACY_TKN_ATTR_ENT_TYPE_: ClassVar[str] = "spacy_tkn_attr_ent_type_"
    _DCR_CFG_SPACY_TKN_ATTR_HEAD: ClassVar[str] = "spacy_tkn_attr_head"
    _DCR_CFG_SPACY_TKN_ATTR_I: ClassVar[str] = "spacy_tkn_attr_i"
    _DCR_CFG_SPACY_TKN_ATTR_IDX: ClassVar[str] = "spacy_tkn_attr_idx"
    _DCR_CFG_SPACY_TKN_ATTR_IS_ALPHA: ClassVar[str] = "spacy_tkn_attr_is_alpha"
    _DCR_CFG_SPACY_TKN_ATTR_IS_ASCII: ClassVar[str] = "spacy_tkn_attr_is_ascii"
    _DCR_CFG_SPACY_TKN_ATTR_IS_BRACKET: ClassVar[str] = "spacy_tkn_attr_is_bracket"
    _DCR_CFG_SPACY_TKN_ATTR_IS_CURRENCY: ClassVar[str] = "spacy_tkn_attr_is_currency"
    _DCR_CFG_SPACY_TKN_ATTR_IS_DIGIT: ClassVar[str] = "spacy_tkn_attr_is_digit"
    _DCR_CFG_SPACY_TKN_ATTR_IS_LEFT_PUNCT: ClassVar[str] = "spacy_tkn_attr_is_left_punct"
    _DCR_CFG_SPACY_TKN_ATTR_IS_LOWER: ClassVar[str] = "spacy_tkn_attr_is_lower"
    _DCR_CFG_SPACY_TKN_ATTR_IS_OOV: ClassVar[str] = "spacy_tkn_attr_is_oov"
    _DCR_CFG_SPACY_TKN_ATTR_IS_PUNCT: ClassVar[str] = "spacy_tkn_attr_is_punct"
    _DCR_CFG_SPACY_TKN_ATTR_IS_QUOTE: ClassVar[str] = "spacy_tkn_attr_is_quote"
    _DCR_CFG_SPACY_TKN_ATTR_IS_RIGHT_PUNCT: ClassVar[str] = "spacy_tkn_attr_is_right_punct"
    _DCR_CFG_SPACY_TKN_ATTR_IS_SENT_END: ClassVar[str] = "spacy_tkn_attr_is_sent_end"
    _DCR_CFG_SPACY_TKN_ATTR_IS_SENT_START: ClassVar[str] = "spacy_tkn_attr_is_sent_start"
    _DCR_CFG_SPACY_TKN_ATTR_IS_SPACE: ClassVar[str] = "spacy_tkn_attr_is_space"
    _DCR_CFG_SPACY_TKN_ATTR_IS_STOP: ClassVar[str] = "spacy_tkn_attr_is_stop"
    _DCR_CFG_SPACY_TKN_ATTR_IS_TITLE: ClassVar[str] = "spacy_tkn_attr_is_title"
    _DCR_CFG_SPACY_TKN_ATTR_IS_UPPER: ClassVar[str] = "spacy_tkn_attr_is_upper"
    _DCR_CFG_SPACY_TKN_ATTR_LANG_: ClassVar[str] = "spacy_tkn_attr_lang_"
    _DCR_CFG_SPACY_TKN_ATTR_LEFT_EDGE: ClassVar[str] = "spacy_tkn_attr_left_edge"
    _DCR_CFG_SPACY_TKN_ATTR_LEMMA_: ClassVar[str] = "spacy_tkn_attr_lemma_"
    _DCR_CFG_SPACY_TKN_ATTR_LEX: ClassVar[str] = "spacy_tkn_attr_lex"
    _DCR_CFG_SPACY_TKN_ATTR_LEX_ID: ClassVar[str] = "spacy_tkn_attr_lex_id"
    _DCR_CFG_SPACY_TKN_ATTR_LIKE_EMAIL: ClassVar[str] = "spacy_tkn_attr_like_email"
    _DCR_CFG_SPACY_TKN_ATTR_LIKE_NUM: ClassVar[str] = "spacy_tkn_attr_like_num"
    _DCR_CFG_SPACY_TKN_ATTR_LIKE_URL: ClassVar[str] = "spacy_tkn_attr_like_url"
    _DCR_CFG_SPACY_TKN_ATTR_LOWER_: ClassVar[str] = "spacy_tkn_attr_lower_"
    _DCR_CFG_SPACY_TKN_ATTR_MORPH: ClassVar[str] = "spacy_tkn_attr_morph"
    _DCR_CFG_SPACY_TKN_ATTR_NORM_: ClassVar[str] = "spacy_tkn_attr_norm_"
    _DCR_CFG_SPACY_TKN_ATTR_ORTH_: ClassVar[str] = "spacy_tkn_attr_orth_"
    _DCR_CFG_SPACY_TKN_ATTR_POS_: ClassVar[str] = "spacy_tkn_attr_pos_"
    _DCR_CFG_SPACY_TKN_ATTR_PREFIX_: ClassVar[str] = "spacy_tkn_attr_prefix_"
    _DCR_CFG_SPACY_TKN_ATTR_PROB: ClassVar[str] = "spacy_tkn_attr_prob"
    _DCR_CFG_SPACY_TKN_ATTR_RANK: ClassVar[str] = "spacy_tkn_attr_rank"
    _DCR_CFG_SPACY_TKN_ATTR_RIGHT_EDGE: ClassVar[str] = "spacy_tkn_attr_right_edge"
    _DCR_CFG_SPACY_TKN_ATTR_SENT: ClassVar[str] = "spacy_tkn_attr_sent"
    _DCR_CFG_SPACY_TKN_ATTR_SENTIMENT: ClassVar[str] = "spacy_tkn_attr_sentiment"
    _DCR_CFG_SPACY_TKN_ATTR_SHAPE_: ClassVar[str] = "spacy_tkn_attr_shape_"
    _DCR_CFG_SPACY_TKN_ATTR_SUFFIX_: ClassVar[str] = "spacy_tkn_attr_suffix_"
    _DCR_CFG_SPACY_TKN_ATTR_TAG_: ClassVar[str] = "spacy_tkn_attr_tag_"
    _DCR_CFG_SPACY_TKN_ATTR_TENSOR: ClassVar[str] = "spacy_tkn_attr_tensor"
    _DCR_CFG_SPACY_TKN_ATTR_TEXT: ClassVar[str] = "spacy_tkn_attr_text"
    _DCR_CFG_SPACY_TKN_ATTR_TEXT_WITH_WS: ClassVar[str] = "spacy_tkn_attr_text_with_ws"
    _DCR_CFG_SPACY_TKN_ATTR_VOCAB: ClassVar[str] = "spacy_tkn_attr_vocab"
    _DCR_CFG_SPACY_TKN_ATTR_WHITESPACE_: ClassVar[str] = "spacy_tkn_attr_whitespace_"

    _DCR_CFG_TESSERACT_TIMEOUT: ClassVar[str] = "tesseract_timeout"
    _DCR_CFG_TOKENIZE_2_JSONFILE: ClassVar[str] = "tokenize_2_jsonfile"
    _DCR_CFG_TOKENIZE_2_XMLFILE: ClassVar[str] = "tokenize_2_xmlfile"
    _DCR_CFG_VERBOSE: ClassVar[str] = "verbose"
    _DCR_CFG_VERBOSE_LT_HEADER_FOOTER: ClassVar[str] = "verbose_lt_header_footer"
    _DCR_CFG_VERBOSE_LT_HEADING: ClassVar[str] = "verbose_lt_heading"
    _DCR_CFG_VERBOSE_LT_LIST_BULLET: ClassVar[str] = "verbose_lt_list_bullet"
    _DCR_CFG_VERBOSE_LT_LIST_NUMBER: ClassVar[str] = "verbose_lt_list_number"
    _DCR_CFG_VERBOSE_LT_TOC: ClassVar[str] = "verbose_lt_toc"
    _DCR_CFG_VERBOSE_PARSER: ClassVar[str] = "verbose_parser"

    _DCR_CORE_ENVIRONMENT_TYPE: ClassVar[str] = "DCR_CORE_ENVIRONMENT_TYPE"

    DCR_VERSION: ClassVar[str] = "0.9.8"

    ENVIRONMENT_TYPE_DEV: ClassVar[str] = "dev"
    ENVIRONMENT_TYPE_PROD: ClassVar[str] = "prod"
    ENVIRONMENT_TYPE_TEST: ClassVar[str] = "test"

    PDF2IMAGE_TYPE_JPEG: ClassVar[str] = "jpeg"
    PDF2IMAGE_TYPE_PNG: ClassVar[str] = "png"

    # ------------------------------------------------------------------
    # Initialise the instance.
    # ------------------------------------------------------------------
    # pylint: disable=too-many-statements
    def __init__(self) -> None:
        """Initialise the instance."""
        try:
            core_glob.logger.debug(core_glob.LOGGER_START)
        except AttributeError:
            core_glob.initialise_logger()
            core_glob.logger.debug(core_glob.LOGGER_START)

        self._get_environment_variant()

        self._config: dict[str, str] = {}

        self._config_parser = configparser.ConfigParser()
        self._config_parser.read(Setup._DCR_CFG_FILE)

        # ------------------------------------------------------------------
        # DCR-CORE configuration.
        # ------------------------------------------------------------------
        self.directory_inbox = "data/inbox_prod"

        self.lt_export_rule_file_heading = "data/lt_export_rule_heading.json"
        self.lt_export_rule_file_list_bullet = "data/lt_export_rule_list_bullet.json"
        self.lt_export_rule_file_list_number = "data/lt_export_rule_list_number.json"

        self.is_delete_auxiliary_files = False

        self.is_json_incl_config = True
        self.is_json_incl_fonts = True
        self.is_json_incl_heading = True
        self.is_json_incl_list_bullet = True
        self.is_json_incl_list_number = True
        self.is_json_incl_params = True

        self.is_json_sort_keys = True

        self.is_lt_footer_required = True
        self.is_lt_header_required = True
        self.is_lt_heading_file_incl_regexp = True
        self.is_lt_heading_required = True
        self.is_lt_list_bullet_required = True
        self.is_lt_list_number_file_incl_regexp = True
        self.is_lt_list_number_required = True
        self.is_lt_toc_required = True

        # ------------------------------------------------------------------
        # Spacy ignore tokens.
        # ------------------------------------------------------------------
        self.is_spacy_ignore_bracket = False
        self.is_spacy_ignore_left_punct = False
        self.is_spacy_ignore_line_type_footer = False
        self.is_spacy_ignore_line_type_header = False
        self.is_spacy_ignore_line_type_heading = False
        self.is_spacy_ignore_line_type_list_bullet = False
        self.is_spacy_ignore_line_type_list_number = False
        self.is_spacy_ignore_line_type_table = False
        self.is_spacy_ignore_line_type_toc = False
        self.is_spacy_ignore_punct = False
        self.is_spacy_ignore_quote = False
        self.is_spacy_ignore_right_punct = False
        self.is_spacy_ignore_space = False
        self.is_spacy_ignore_stop = False

        # ------------------------------------------------------------------
        # spaCy token attributes.
        # ------------------------------------------------------------------
        self.is_spacy_tkn_attr_cluster = True
        self.is_spacy_tkn_attr_dep_ = True
        self.is_spacy_tkn_attr_doc = True
        self.is_spacy_tkn_attr_ent_iob_ = True
        self.is_spacy_tkn_attr_ent_kb_id_ = True
        self.is_spacy_tkn_attr_ent_type_ = True
        self.is_spacy_tkn_attr_head = True
        self.is_spacy_tkn_attr_i = True
        self.is_spacy_tkn_attr_idx = True
        self.is_spacy_tkn_attr_is_alpha = True
        self.is_spacy_tkn_attr_is_ascii = True
        self.is_spacy_tkn_attr_is_bracket = True
        self.is_spacy_tkn_attr_is_currency = True
        self.is_spacy_tkn_attr_is_digit = True
        self.is_spacy_tkn_attr_is_left_punct = True
        self.is_spacy_tkn_attr_is_lower = True
        self.is_spacy_tkn_attr_is_oov = True
        self.is_spacy_tkn_attr_is_punct = True
        self.is_spacy_tkn_attr_is_quote = True
        self.is_spacy_tkn_attr_is_right_punct = True
        self.is_spacy_tkn_attr_is_sent_end = True
        self.is_spacy_tkn_attr_is_sent_start = True
        self.is_spacy_tkn_attr_is_space = True
        self.is_spacy_tkn_attr_is_stop = True
        self.is_spacy_tkn_attr_is_title = True
        self.is_spacy_tkn_attr_is_upper = True
        self.is_spacy_tkn_attr_lang_ = True
        self.is_spacy_tkn_attr_left_edge = True
        self.is_spacy_tkn_attr_lemma_ = True
        self.is_spacy_tkn_attr_lex = True
        self.is_spacy_tkn_attr_lex_id = True
        self.is_spacy_tkn_attr_like_email = True
        self.is_spacy_tkn_attr_like_num = True
        self.is_spacy_tkn_attr_like_url = True
        self.is_spacy_tkn_attr_lower_ = True
        self.is_spacy_tkn_attr_morph = True
        self.is_spacy_tkn_attr_norm_ = True
        self.is_spacy_tkn_attr_orth_ = True
        self.is_spacy_tkn_attr_pos_ = True
        self.is_spacy_tkn_attr_prefix_ = True
        self.is_spacy_tkn_attr_prob = True
        self.is_spacy_tkn_attr_rank = True
        self.is_spacy_tkn_attr_right_edge = True
        self.is_spacy_tkn_attr_sent = True
        self.is_spacy_tkn_attr_sentiment = True
        self.is_spacy_tkn_attr_shape_ = True
        self.is_spacy_tkn_attr_suffix_ = True
        self.is_spacy_tkn_attr_tag_ = True
        self.is_spacy_tkn_attr_tensor = True
        self.is_spacy_tkn_attr_text = True
        self.is_spacy_tkn_attr_text_with_ws = True
        self.is_spacy_tkn_attr_vocab = True
        self.is_spacy_tkn_attr_whitespace_ = True

        self.is_tokenize_2_jsonfile = True
        self.is_tokenize_2_xmlfile = True

        self.is_verbose = True
        self.is_verbose_lt_header_footer = False
        self.is_verbose_lt_heading = False
        self.is_verbose_lt_list_bullet = False
        self.is_verbose_lt_list_number = False
        self.is_verbose_lt_toc = False

        self.json_indent = 4

        self.lt_footer_max_distance = 3
        self.lt_footer_max_lines = 3
        self.lt_header_max_distance = 3
        self.lt_header_max_lines = 3
        self.lt_heading_file_incl_no_ctx = 1
        self.lt_heading_max_level = 3
        self.lt_heading_min_pages = 2
        self.lt_heading_rule_file = "none"
        self.lt_heading_tolerance_llx = 10
        self.lt_list_bullet_min_entries = 2
        self.lt_list_bullet_rule_file = "none"
        self.lt_list_bullet_tolerance_llx = 10
        self.lt_list_number_min_entries = 2
        self.lt_list_number_rule_file = "none"
        self.lt_list_number_tolerance_llx = 10
        self.lt_toc_last_page = 5
        self.lt_toc_min_entries = 5

        self.pdf2image_type = "jpeg"

        self.tesseract_timeout = 30
        self.verbose_parser = "none"

        self._load_config()

        core_utils.progress_msg_core("The configuration parameters (dcr_core) are checked and loaded")

        self._exist = True

        core_glob.logger.debug(core_glob.LOGGER_END)

    # ------------------------------------------------------------------
    # Check the configuration parameters.
    # ------------------------------------------------------------------
    # pylint: disable=too-many-branches
    def _check_config(self) -> None:  # noqa: C901
        """Check the configuration parameters."""
        core_glob.logger.debug(core_glob.LOGGER_START)

        if Setup._DCR_CFG_DELETE_AUXILIARY_FILES in self._config:
            self.is_delete_auxiliary_files = self._determine_config_param_boolean(
                Setup._DCR_CFG_DELETE_AUXILIARY_FILES, self.is_delete_auxiliary_files
            )

        if Setup._DCR_CFG_DIRECTORY_INBOX in self._config:
            self._check_config_directory_inbox()

        if Setup._DCR_CFG_JSON_INCL_CONFIG in self._config:
            self.is_json_incl_config = self._determine_config_param_boolean(Setup._DCR_CFG_JSON_INCL_CONFIG, self.is_json_incl_config)

        if Setup._DCR_CFG_JSON_INCL_FONTS in self._config:
            self.is_json_incl_fonts = self._determine_config_param_boolean(Setup._DCR_CFG_JSON_INCL_FONTS, self.is_json_incl_fonts)

        if Setup._DCR_CFG_JSON_INCL_HEADING in self._config:
            self.is_json_incl_heading = self._determine_config_param_boolean(Setup._DCR_CFG_JSON_INCL_HEADING, self.is_json_incl_heading)

        if Setup._DCR_CFG_JSON_INCL_LIST_BULLET in self._config:
            self.is_json_incl_list_bullet = self._determine_config_param_boolean(
                Setup._DCR_CFG_JSON_INCL_LIST_BULLET, self.is_json_incl_list_bullet
            )

        if Setup._DCR_CFG_JSON_INCL_LIST_NUMBER in self._config:
            self.is_json_incl_list_number = self._determine_config_param_boolean(
                Setup._DCR_CFG_JSON_INCL_LIST_NUMBER, self.is_json_incl_list_number
            )

        if Setup._DCR_CFG_JSON_INCL_PARAMS in self._config:
            self.is_json_incl_params = self._determine_config_param_boolean(Setup._DCR_CFG_JSON_INCL_PARAMS, self.is_json_incl_params)

        if Setup._DCR_CFG_JSON_INDENT in self._config:
            self.json_indent = self._determine_config_param_integer(Setup._DCR_CFG_JSON_INDENT, self.json_indent)

        if Setup._DCR_CFG_JSON_SORT_KEYS in self._config:
            self.is_json_sort_keys = self._determine_config_param_boolean(Setup._DCR_CFG_JSON_SORT_KEYS, self.is_json_sort_keys)

        if Setup._DCR_CFG_LT_FOOTER_MAX_DISTANCE in self._config:
            self.lt_footer_max_distance = self._determine_config_param_integer(
                Setup._DCR_CFG_LT_FOOTER_MAX_DISTANCE, self.lt_footer_max_distance
            )

        if Setup._DCR_CFG_LT_FOOTER_MAX_LINES in self._config:
            self.lt_footer_max_lines = self._determine_config_param_integer(Setup._DCR_CFG_LT_FOOTER_MAX_LINES, self.lt_footer_max_lines)

        if Setup._DCR_CFG_LT_FOOTER_REQUIRED in self._config:
            self.is_lt_footer_required = self._determine_config_param_boolean(Setup._DCR_CFG_LT_FOOTER_REQUIRED, self.is_lt_footer_required)

        if Setup._DCR_CFG_LT_HEADER_MAX_DISTANCE in self._config:
            self.lt_header_max_distance = self._determine_config_param_integer(
                Setup._DCR_CFG_LT_HEADER_MAX_DISTANCE, self.lt_header_max_distance
            )

        if Setup._DCR_CFG_LT_HEADER_MAX_LINES in self._config:
            self.lt_header_max_lines = self._determine_config_param_integer(Setup._DCR_CFG_LT_HEADER_MAX_LINES, self.lt_header_max_lines)

        if Setup._DCR_CFG_LT_HEADER_REQUIRED in self._config:
            self.is_lt_header_required = self._determine_config_param_boolean(Setup._DCR_CFG_LT_HEADER_REQUIRED, self.is_lt_header_required)

        if Setup._DCR_CFG_LT_HEADING_FILE_INCL_NO_CTX in self._config:
            self.lt_heading_file_incl_no_ctx = self._determine_config_param_integer(
                Setup._DCR_CFG_LT_HEADING_FILE_INCL_NO_CTX, self.lt_heading_file_incl_no_ctx
            )

        if Setup._DCR_CFG_LT_HEADING_FILE_INCL_REGEXP in self._config:
            self.is_lt_heading_file_incl_regexp = self._determine_config_param_boolean(
                Setup._DCR_CFG_LT_HEADING_FILE_INCL_REGEXP, self.is_lt_heading_file_incl_regexp
            )

        if Setup._DCR_CFG_LT_HEADING_MAX_LEVEL in self._config:
            self.lt_heading_max_level = self._determine_config_param_integer(Setup._DCR_CFG_LT_HEADING_MAX_LEVEL, self.lt_heading_max_level)

        if Setup._DCR_CFG_LT_HEADING_MIN_PAGES in self._config:
            self.lt_heading_min_pages = self._determine_config_param_integer(Setup._DCR_CFG_LT_HEADING_MIN_PAGES, self.lt_heading_min_pages)

        if Setup._DCR_CFG_LT_HEADING_REQUIRED in self._config:
            self.is_lt_heading_required = self._determine_config_param_boolean(
                Setup._DCR_CFG_LT_HEADING_REQUIRED, self.is_lt_heading_required
            )

        if Setup._DCR_CFG_LT_HEADING_TOLERANCE_LLX in self._config:
            self.lt_heading_tolerance_llx = self._determine_config_param_integer(
                Setup._DCR_CFG_LT_HEADING_TOLERANCE_LLX, self.lt_heading_tolerance_llx
            )

        if Setup._DCR_CFG_LT_LIST_BULLET_MIN_ENTRIES in self._config:
            self.lt_list_bullet_min_entries = self._determine_config_param_integer(
                Setup._DCR_CFG_LT_LIST_BULLET_MIN_ENTRIES, self.lt_list_bullet_min_entries
            )

        if Setup._DCR_CFG_LT_LIST_BULLET_REQUIRED in self._config:
            self.is_lt_list_bullet_required = self._determine_config_param_boolean(
                Setup._DCR_CFG_LT_LIST_BULLET_REQUIRED, self.is_lt_list_bullet_required
            )

        if Setup._DCR_CFG_LT_LIST_BULLET_TOLERANCE_LLX in self._config:
            self.lt_list_bullet_tolerance_llx = self._determine_config_param_integer(
                Setup._DCR_CFG_LT_LIST_BULLET_TOLERANCE_LLX, self.lt_list_bullet_tolerance_llx
            )

        if Setup._DCR_CFG_LT_LIST_NUMBER_FILE_INCL_REGEXP in self._config:
            self.is_lt_list_number_file_incl_regexp = self._determine_config_param_boolean(
                Setup._DCR_CFG_LT_LIST_NUMBER_FILE_INCL_REGEXP, self.is_lt_list_number_file_incl_regexp
            )

        if Setup._DCR_CFG_LT_LIST_NUMBER_MIN_ENTRIES in self._config:
            self.lt_list_number_min_entries = self._determine_config_param_integer(
                Setup._DCR_CFG_LT_LIST_NUMBER_MIN_ENTRIES, self.lt_list_number_min_entries
            )

        if Setup._DCR_CFG_LT_LIST_NUMBER_REQUIRED in self._config:
            self.is_lt_list_number_required = self._determine_config_param_boolean(
                Setup._DCR_CFG_LT_LIST_NUMBER_REQUIRED, self.is_lt_list_number_required
            )

        if Setup._DCR_CFG_LT_LIST_NUMBER_TOLERANCE_LLX in self._config:
            self.lt_list_number_tolerance_llx = self._determine_config_param_integer(
                Setup._DCR_CFG_LT_LIST_NUMBER_TOLERANCE_LLX, self.lt_list_number_tolerance_llx
            )

        if Setup._DCR_CFG_LT_TOC_LAST_PAGE in self._config:
            self.lt_toc_last_page = self._determine_config_param_integer(Setup._DCR_CFG_LT_TOC_LAST_PAGE, self.lt_toc_last_page)

        if Setup._DCR_CFG_LT_TOC_MIN_ENTRIES in self._config:
            self.lt_toc_min_entries = self._determine_config_param_integer(Setup._DCR_CFG_LT_TOC_MIN_ENTRIES, self.lt_toc_min_entries)

        if Setup._DCR_CFG_LT_TOC_REQUIRED in self._config:
            self.is_lt_toc_required = self._determine_config_param_boolean(Setup._DCR_CFG_LT_TOC_REQUIRED, self.is_lt_toc_required)

        if Setup._DCR_CFG_PDF2IMAGE_TYPE in self._config:
            self._check_config_pdf2image_type()

        self._determine_config_spacy_tkn()

        self._determine_config_spacy_tkn_ignore()

        if Setup._DCR_CFG_TESSERACT_TIMEOUT in self._config:
            self.tesseract_timeout = self._determine_config_param_integer(Setup._DCR_CFG_TESSERACT_TIMEOUT, self.tesseract_timeout)

        if Setup._DCR_CFG_TOKENIZE_2_JSONFILE in self._config:
            self.is_tokenize_2_jsonfile = self._determine_config_param_boolean(
                Setup._DCR_CFG_TOKENIZE_2_JSONFILE, self.is_tokenize_2_jsonfile
            )

        if Setup._DCR_CFG_TOKENIZE_2_XMLFILE in self._config:
            self.is_tokenize_2_xmlfile = self._determine_config_param_boolean(Setup._DCR_CFG_TOKENIZE_2_XMLFILE, self.is_tokenize_2_xmlfile)

        if Setup._DCR_CFG_VERBOSE in self._config:
            self.is_verbose = self._determine_config_param_boolean(Setup._DCR_CFG_VERBOSE, self.is_verbose)

        if Setup._DCR_CFG_VERBOSE_LT_HEADER_FOOTER in self._config:
            self.is_verbose_lt_header_footer = self._determine_config_param_boolean(
                Setup._DCR_CFG_VERBOSE_LT_HEADER_FOOTER, self.is_verbose_lt_header_footer
            )

        if Setup._DCR_CFG_VERBOSE_LT_HEADING in self._config:
            self.is_verbose_lt_heading = self._determine_config_param_boolean(Setup._DCR_CFG_VERBOSE_LT_HEADING, self.is_verbose_lt_heading)

        if Setup._DCR_CFG_VERBOSE_LT_LIST_BULLET in self._config:
            self.is_verbose_lt_list_bullet = self._determine_config_param_boolean(
                Setup._DCR_CFG_VERBOSE_LT_LIST_BULLET, self.is_verbose_lt_list_bullet
            )

        if Setup._DCR_CFG_VERBOSE_LT_LIST_NUMBER in self._config:
            self.is_verbose_lt_list_number = self._determine_config_param_boolean(
                Setup._DCR_CFG_VERBOSE_LT_LIST_NUMBER, self.is_verbose_lt_list_number
            )

        if Setup._DCR_CFG_VERBOSE_LT_TOC in self._config:
            self.is_verbose_lt_toc = self._determine_config_param_boolean(Setup._DCR_CFG_VERBOSE_LT_TOC, self.is_verbose_lt_toc)

        if Setup._DCR_CFG_VERBOSE_PARSER in self._config:
            self._check_config_verbose_parser()

        core_glob.logger.debug(core_glob.LOGGER_END)

    # -----------------------------------------------------------------------------
    # Check the configuration parameter - directory_inbox.
    # -----------------------------------------------------------------------------
    def _check_config_directory_inbox(self) -> None:
        """Check the configuration parameter - directory_inbox."""
        if Setup._DCR_CFG_DIRECTORY_INBOX in self._config:
            self._config[Setup._DCR_CFG_DIRECTORY_INBOX] = str(self._config[Setup._DCR_CFG_DIRECTORY_INBOX])

            self.directory_inbox = core_utils.get_os_independent_name(str(self._config[Setup._DCR_CFG_DIRECTORY_INBOX]))
        else:
            core_utils.terminate_fatal(f"Missing configuration parameter '{Setup._DCR_CFG_DIRECTORY_INBOX}'")

    # ------------------------------------------------------------------
    # Check the configuration parameter - pdf2image_type.
    # ------------------------------------------------------------------
    def _check_config_pdf2image_type(self) -> None:
        """Check the configuration parameter - pdf2image_type."""
        if Setup._DCR_CFG_PDF2IMAGE_TYPE in self._config:
            self.pdf2image_type = str(self._config[Setup._DCR_CFG_PDF2IMAGE_TYPE])
            if self.pdf2image_type not in [
                Setup.PDF2IMAGE_TYPE_JPEG,
                Setup.PDF2IMAGE_TYPE_PNG,
            ]:
                core_utils.terminate_fatal(
                    f"Invalid configuration parameter value for parameter " f"'pdf2image_type': '{self.pdf2image_type}'"
                )

    # ------------------------------------------------------------------
    # Check the configuration parameter - verbose_parser.
    # ------------------------------------------------------------------
    def _check_config_verbose_parser(self) -> None:
        """Check the configuration parameter - verbose_parser."""
        if Setup._DCR_CFG_VERBOSE_PARSER in self._config:
            if str(self._config[Setup._DCR_CFG_VERBOSE_PARSER]).lower() in {"all", "text"}:
                self.verbose_parser = str(self._config[Setup._DCR_CFG_VERBOSE_PARSER]).lower()

    # ------------------------------------------------------------------
    # Determine a boolean configuration parameter.
    # ------------------------------------------------------------------
    def _determine_config_param_boolean(
        self,
        param: str,
        var: bool,
    ) -> bool:
        """Determine a boolean configuration parameter.

        Args:
            param (str): Parameter name.
            var (bool): Default parameter value.

        Returns:
            bool: Specified value.
        """
        if var and param in self._config:
            if str(self._config[param]).lower() == "false":
                return False
        elif not var and param in self._config:
            if str(self._config[param]).lower() == "true":
                return True

        return var

    # ------------------------------------------------------------------
    # Determine a integer configuration parameter.
    # ------------------------------------------------------------------
    def _determine_config_param_integer(
        self,
        param: str,
        var: int,
    ) -> int:
        """Determine a integer configuration parameter.

        Args:
            param (str): Parameter name.
            var (int): Default parameter value.

        Returns:
            int: Specified value.
        """
        if param in self._config:
            return int(str(self._config[param]))

        return var

    # ------------------------------------------------------------------
    # Determine a spaCy token configuration parameter.
    # ------------------------------------------------------------------
    # pylint: disable=too-many-branches
    def _determine_config_spacy_tkn(self) -> None:  # noqa: C901
        """Determine a spaCy token configuration parameter."""
        if Setup._DCR_CFG_SPACY_TKN_ATTR_CLUSTER in self._config:
            self.is_spacy_tkn_attr_cluster = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_CLUSTER, self.is_spacy_tkn_attr_cluster
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_DEP_ in self._config:
            self.is_spacy_tkn_attr_dep_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_DEP_, self.is_spacy_tkn_attr_dep_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_DOC in self._config:
            self.is_spacy_tkn_attr_doc = self._determine_config_param_boolean(Setup._DCR_CFG_SPACY_TKN_ATTR_DOC, self.is_spacy_tkn_attr_doc)

        if Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_IOB_ in self._config:
            self.is_spacy_tkn_attr_ent_iob_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_IOB_, self.is_spacy_tkn_attr_ent_iob_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_KB_ID_ in self._config:
            self.is_spacy_tkn_attr_ent_kb_id_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_KB_ID_, self.is_spacy_tkn_attr_ent_kb_id_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_TYPE_ in self._config:
            self.is_spacy_tkn_attr_ent_type_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_TYPE_, self.is_spacy_tkn_attr_ent_type_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_HEAD in self._config:
            self.is_spacy_tkn_attr_head = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_HEAD, self.is_spacy_tkn_attr_head
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_I in self._config:
            self.is_spacy_tkn_attr_i = self._determine_config_param_boolean(Setup._DCR_CFG_SPACY_TKN_ATTR_I, self.is_spacy_tkn_attr_i)

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IDX in self._config:
            self.is_spacy_tkn_attr_idx = self._determine_config_param_boolean(Setup._DCR_CFG_SPACY_TKN_ATTR_IDX, self.is_spacy_tkn_attr_idx)

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ALPHA in self._config:
            self.is_spacy_tkn_attr_is_alpha = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ALPHA, self.is_spacy_tkn_attr_is_alpha
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ASCII in self._config:
            self.is_spacy_tkn_attr_is_ascii = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ASCII, self.is_spacy_tkn_attr_is_ascii
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_BRACKET in self._config:
            self.is_spacy_tkn_attr_is_bracket = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_BRACKET, self.is_spacy_tkn_attr_is_bracket
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_CURRENCY in self._config:
            self.is_spacy_tkn_attr_is_currency = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_CURRENCY, self.is_spacy_tkn_attr_is_currency
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_DIGIT in self._config:
            self.is_spacy_tkn_attr_is_digit = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_DIGIT, self.is_spacy_tkn_attr_is_digit
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LEFT_PUNCT in self._config:
            self.is_spacy_tkn_attr_is_left_punct = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LEFT_PUNCT, self.is_spacy_tkn_attr_is_left_punct
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LOWER in self._config:
            self.is_spacy_tkn_attr_is_lower = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LOWER, self.is_spacy_tkn_attr_is_lower
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_OOV in self._config:
            self.is_spacy_tkn_attr_is_oov = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_OOV, self.is_spacy_tkn_attr_is_oov
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_PUNCT in self._config:
            self.is_spacy_tkn_attr_is_punct = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_PUNCT, self.is_spacy_tkn_attr_is_punct
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_QUOTE in self._config:
            self.is_spacy_tkn_attr_is_quote = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_QUOTE, self.is_spacy_tkn_attr_is_quote
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_RIGHT_PUNCT in self._config:
            self.is_spacy_tkn_attr_is_right_punct = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_RIGHT_PUNCT, self.is_spacy_tkn_attr_is_right_punct
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_END in self._config:
            self.is_spacy_tkn_attr_is_sent_end = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_END, self.is_spacy_tkn_attr_is_sent_end
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_START in self._config:
            self.is_spacy_tkn_attr_is_sent_start = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_START, self.is_spacy_tkn_attr_is_sent_start
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SPACE in self._config:
            self.is_spacy_tkn_attr_is_space = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SPACE, self.is_spacy_tkn_attr_is_space
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_STOP in self._config:
            self.is_spacy_tkn_attr_is_stop = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_STOP, self.is_spacy_tkn_attr_is_stop
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_TITLE in self._config:
            self.is_spacy_tkn_attr_is_title = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_TITLE, self.is_spacy_tkn_attr_is_title
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_IS_UPPER in self._config:
            self.is_spacy_tkn_attr_is_upper = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_IS_UPPER, self.is_spacy_tkn_attr_is_upper
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_LANG_ in self._config:
            self.is_spacy_tkn_attr_lang_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_LANG_, self.is_spacy_tkn_attr_lang_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_LEFT_EDGE in self._config:
            self.is_spacy_tkn_attr_left_edge = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_LEFT_EDGE, self.is_spacy_tkn_attr_left_edge
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_LEMMA_ in self._config:
            self.is_spacy_tkn_attr_lemma_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_LEMMA_, self.is_spacy_tkn_attr_lemma_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_LEX in self._config:
            self.is_spacy_tkn_attr_lex = self._determine_config_param_boolean(Setup._DCR_CFG_SPACY_TKN_ATTR_LEX, self.is_spacy_tkn_attr_lex)

        if Setup._DCR_CFG_SPACY_TKN_ATTR_LEX_ID in self._config:
            self.is_spacy_tkn_attr_lex_id = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_LEX_ID, self.is_spacy_tkn_attr_lex_id
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_EMAIL in self._config:
            self.is_spacy_tkn_attr_like_email = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_EMAIL, self.is_spacy_tkn_attr_like_email
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_NUM in self._config:
            self.is_spacy_tkn_attr_like_num = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_NUM, self.is_spacy_tkn_attr_like_num
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_URL in self._config:
            self.is_spacy_tkn_attr_like_url = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_URL, self.is_spacy_tkn_attr_like_url
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_LOWER_ in self._config:
            self.is_spacy_tkn_attr_lower_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_LOWER_, self.is_spacy_tkn_attr_lower_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_MORPH in self._config:
            self.is_spacy_tkn_attr_morph = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_MORPH, self.is_spacy_tkn_attr_morph
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_NORM_ in self._config:
            self.is_spacy_tkn_attr_norm_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_NORM_, self.is_spacy_tkn_attr_norm_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_ORTH_ in self._config:
            self.is_spacy_tkn_attr_orth_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_ORTH_, self.is_spacy_tkn_attr_orth_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_POS_ in self._config:
            self.is_spacy_tkn_attr_pos_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_POS_, self.is_spacy_tkn_attr_pos_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_PREFIX_ in self._config:
            self.is_spacy_tkn_attr_prefix_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_PREFIX_, self.is_spacy_tkn_attr_prefix_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_PROB in self._config:
            self.is_spacy_tkn_attr_prob = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_PROB, self.is_spacy_tkn_attr_prob
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_RANK in self._config:
            self.is_spacy_tkn_attr_rank = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_RANK, self.is_spacy_tkn_attr_rank
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_RIGHT_EDGE in self._config:
            self.is_spacy_tkn_attr_right_edge = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_RIGHT_EDGE, self.is_spacy_tkn_attr_right_edge
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_SENT in self._config:
            self.is_spacy_tkn_attr_sent = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_SENT, self.is_spacy_tkn_attr_sent
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_SENTIMENT in self._config:
            self.is_spacy_tkn_attr_sentiment = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_SENTIMENT, self.is_spacy_tkn_attr_sentiment
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_SHAPE_ in self._config:
            self.is_spacy_tkn_attr_shape_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_SHAPE_, self.is_spacy_tkn_attr_shape_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_SUFFIX_ in self._config:
            self.is_spacy_tkn_attr_suffix_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_SUFFIX_, self.is_spacy_tkn_attr_suffix_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_TAG_ in self._config:
            self.is_spacy_tkn_attr_tag_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_TAG_, self.is_spacy_tkn_attr_tag_
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_TENSOR in self._config:
            self.is_spacy_tkn_attr_tensor = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_TENSOR, self.is_spacy_tkn_attr_tensor
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT in self._config:
            self.is_spacy_tkn_attr_text = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT, self.is_spacy_tkn_attr_text
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT_WITH_WS in self._config:
            self.is_spacy_tkn_attr_text_with_ws = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT_WITH_WS, self.is_spacy_tkn_attr_text_with_ws
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_VOCAB in self._config:
            self.is_spacy_tkn_attr_vocab = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_VOCAB, self.is_spacy_tkn_attr_vocab
            )

        if Setup._DCR_CFG_SPACY_TKN_ATTR_WHITESPACE_ in self._config:
            self.is_spacy_tkn_attr_whitespace_ = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_TKN_ATTR_WHITESPACE_, self.is_spacy_tkn_attr_whitespace_
            )

    # ------------------------------------------------------------------
    # Determine a spaCy token configuration parameter to ignore the token creation.
    # ------------------------------------------------------------------
    def _determine_config_spacy_tkn_ignore(self) -> None:  # noqa: C901
        """Determine if the token creation is not required."""
        if Setup._DCR_CFG_SPACY_IGNORE_BRACKET in self._config:
            self.is_spacy_ignore_bracket = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_IGNORE_BRACKET, self.is_spacy_ignore_bracket
            )

        if Setup._DCR_CFG_SPACY_IGNORE_LEFT_PUNCT in self._config:
            self.is_spacy_ignore_left_punct = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_IGNORE_LEFT_PUNCT, self.is_spacy_ignore_left_punct
            )

        if Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_FOOTER in self._config:
            self.is_spacy_ignore_line_type_footer = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_FOOTER, self.is_spacy_ignore_line_type_footer
            )

        if Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_HEADER in self._config:
            self.is_spacy_ignore_line_type_header = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_HEADER, self.is_spacy_ignore_line_type_header
            )

        if Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_HEADING in self._config:
            self.is_spacy_ignore_line_type_heading = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_HEADING, self.is_spacy_ignore_line_type_heading
            )

        if Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_LIST_BULLET in self._config:
            self.is_spacy_ignore_line_type_list_bullet = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_LIST_BULLET, self.is_spacy_ignore_line_type_list_bullet
            )

        if Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_LIST_NUMBER in self._config:
            self.is_spacy_ignore_line_type_list_number = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_LIST_NUMBER, self.is_spacy_ignore_line_type_list_number
            )

        if Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_TABLE in self._config:
            self.is_spacy_ignore_line_type_table = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_TABLE, self.is_spacy_ignore_line_type_table
            )

        if Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_TOC in self._config:
            self.is_spacy_ignore_line_type_toc = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_TOC, self.is_spacy_ignore_line_type_toc
            )

        if Setup._DCR_CFG_SPACY_IGNORE_PUNCT in self._config:
            self.is_spacy_ignore_punct = self._determine_config_param_boolean(Setup._DCR_CFG_SPACY_IGNORE_PUNCT, self.is_spacy_ignore_punct)

        if Setup._DCR_CFG_SPACY_IGNORE_QUOTE in self._config:
            self.is_spacy_ignore_quote = self._determine_config_param_boolean(Setup._DCR_CFG_SPACY_IGNORE_QUOTE, self.is_spacy_ignore_quote)

        if Setup._DCR_CFG_SPACY_IGNORE_RIGHT_PUNCT in self._config:
            self.is_spacy_ignore_right_punct = self._determine_config_param_boolean(
                Setup._DCR_CFG_SPACY_IGNORE_RIGHT_PUNCT, self.is_spacy_ignore_right_punct
            )

        if Setup._DCR_CFG_SPACY_IGNORE_SPACE in self._config:
            self.is_spacy_ignore_space = self._determine_config_param_boolean(Setup._DCR_CFG_SPACY_IGNORE_SPACE, self.is_spacy_ignore_space)

        if Setup._DCR_CFG_SPACY_IGNORE_STOP in self._config:
            self.is_spacy_ignore_stop = self._determine_config_param_boolean(Setup._DCR_CFG_SPACY_IGNORE_STOP, self.is_spacy_ignore_stop)

    # ------------------------------------------------------------------
    # Determine and check the environment variant.
    # ------------------------------------------------------------------
    def _get_environment_variant(self) -> None:
        """Determine and check the environment variant."""
        self.environment_variant = Setup.ENVIRONMENT_TYPE_PROD

        try:
            self.environment_variant = os.environ[Setup._DCR_CORE_ENVIRONMENT_TYPE]
        except KeyError:
            self.environment_variant = Setup.ENVIRONMENT_TYPE_PROD

        if self.environment_variant not in [
            Setup.ENVIRONMENT_TYPE_DEV,
            Setup.ENVIRONMENT_TYPE_PROD,
            Setup.ENVIRONMENT_TYPE_TEST,
        ]:
            core_utils.terminate_fatal(
                f"The environment variable '{Setup._DCR_CORE_ENVIRONMENT_TYPE}' " f"has the invalid content '{self.environment_variant}'"
            )

    # ------------------------------------------------------------------
    # Load and check the configuration parameters.
    # ------------------------------------------------------------------
    def _load_config(self) -> None:
        """Load and check the configuration parameters."""
        core_glob.logger.debug(core_glob.LOGGER_START)

        for section in self._config_parser.sections():
            if section in (
                Setup._DCR_CFG_SECTION_CORE,
                Setup._DCR_CFG_SECTION_CORE + ".env." + self.environment_variant,
                Setup._DCR_CFG_SECTION_CORE_SPACY,
            ):
                for (key, value) in self._config_parser.items(section):
                    self._config[key] = value

                for key, item in self._config.items():
                    match key:
                        case (
                            Setup._DCR_CFG_DELETE_AUXILIARY_FILES
                            | Setup._DCR_CFG_DIRECTORY_INBOX
                            | Setup._DCR_CFG_JSON_INCL_CONFIG
                            | Setup._DCR_CFG_JSON_INCL_FONTS
                            | Setup._DCR_CFG_JSON_INCL_HEADING
                            | Setup._DCR_CFG_JSON_INCL_LIST_BULLET
                            | Setup._DCR_CFG_JSON_INCL_LIST_NUMBER
                            | Setup._DCR_CFG_JSON_INCL_PARAMS
                            | Setup._DCR_CFG_JSON_INDENT
                            | Setup._DCR_CFG_JSON_SORT_KEYS
                            | Setup._DCR_CFG_LT_FOOTER_MAX_DISTANCE
                            | Setup._DCR_CFG_LT_FOOTER_MAX_LINES
                            | Setup._DCR_CFG_LT_FOOTER_REQUIRED
                            | Setup._DCR_CFG_LT_HEADER_MAX_DISTANCE
                            | Setup._DCR_CFG_LT_HEADER_MAX_LINES
                            | Setup._DCR_CFG_LT_HEADER_REQUIRED
                            | Setup._DCR_CFG_LT_HEADING_FILE_INCL_NO_CTX
                            | Setup._DCR_CFG_LT_HEADING_FILE_INCL_REGEXP
                            | Setup._DCR_CFG_LT_HEADING_MAX_LEVEL
                            | Setup._DCR_CFG_LT_HEADING_MIN_PAGES
                            | Setup._DCR_CFG_LT_HEADING_REQUIRED
                            | Setup._DCR_CFG_LT_HEADING_TOLERANCE_LLX
                            | Setup._DCR_CFG_LT_LIST_BULLET_MIN_ENTRIES
                            | Setup._DCR_CFG_LT_LIST_BULLET_REQUIRED
                            | Setup._DCR_CFG_LT_LIST_BULLET_TOLERANCE_LLX
                            | Setup._DCR_CFG_LT_LIST_NUMBER_FILE_INCL_REGEXP
                            | Setup._DCR_CFG_LT_LIST_NUMBER_MIN_ENTRIES
                            | Setup._DCR_CFG_LT_LIST_NUMBER_REQUIRED
                            | Setup._DCR_CFG_LT_LIST_NUMBER_TOLERANCE_LLX
                            | Setup._DCR_CFG_LT_TOC_LAST_PAGE
                            | Setup._DCR_CFG_LT_TOC_MIN_ENTRIES
                            | Setup._DCR_CFG_LT_TOC_REQUIRED
                            | Setup._DCR_CFG_PDF2IMAGE_TYPE
                            | Setup._DCR_CFG_SPACY_IGNORE_BRACKET
                            | Setup._DCR_CFG_SPACY_IGNORE_LEFT_PUNCT
                            | Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_FOOTER
                            | Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_HEADER
                            | Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_HEADING
                            | Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_LIST_BULLET
                            | Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_LIST_NUMBER
                            | Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_TABLE
                            | Setup._DCR_CFG_SPACY_IGNORE_LINE_TYPE_TOC
                            | Setup._DCR_CFG_SPACY_IGNORE_PUNCT
                            | Setup._DCR_CFG_SPACY_IGNORE_QUOTE
                            | Setup._DCR_CFG_SPACY_IGNORE_RIGHT_PUNCT
                            | Setup._DCR_CFG_SPACY_IGNORE_SPACE
                            | Setup._DCR_CFG_SPACY_IGNORE_STOP
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_CLUSTER
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_DEP_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_DOC
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_IOB_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_KB_ID_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_ENT_TYPE_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_HEAD
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_I
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IDX
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ALPHA
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_ASCII
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_BRACKET
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_CURRENCY
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_DIGIT
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LEFT_PUNCT
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_LOWER
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_OOV
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_PUNCT
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_QUOTE
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_RIGHT_PUNCT
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_END
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SENT_START
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_SPACE
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_STOP
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_TITLE
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_IS_UPPER
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_LANG_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_LEFT_EDGE
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_LEMMA_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_LEX
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_LEX_ID
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_EMAIL
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_NUM
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_LIKE_URL
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_LOWER_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_MORPH
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_NORM_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_ORTH_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_POS_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_PREFIX_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_PROB
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_RANK
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_RIGHT_EDGE
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_SENT
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_SENTIMENT
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_SHAPE_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_SUFFIX_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_TAG_
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_TENSOR
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_TEXT_WITH_WS
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_VOCAB
                            | Setup._DCR_CFG_SPACY_TKN_ATTR_WHITESPACE_
                            | Setup._DCR_CFG_TESSERACT_TIMEOUT
                            | Setup._DCR_CFG_TOKENIZE_2_JSONFILE
                            | Setup._DCR_CFG_TOKENIZE_2_XMLFILE
                            | Setup._DCR_CFG_VERBOSE
                            | Setup._DCR_CFG_VERBOSE_LT_HEADER_FOOTER
                            | Setup._DCR_CFG_VERBOSE_LT_HEADING
                            | Setup._DCR_CFG_VERBOSE_LT_LIST_BULLET
                            | Setup._DCR_CFG_VERBOSE_LT_LIST_NUMBER
                            | Setup._DCR_CFG_VERBOSE_LT_TOC
                            | Setup._DCR_CFG_VERBOSE_PARSER
                        ):
                            continue
                        case Setup._DCR_CFG_LT_HEADING_RULE_FILE:
                            self.lt_heading_rule_file = core_utils.get_os_independent_name(item)
                        case Setup._DCR_CFG_LT_LIST_BULLET_RULE_FILE:
                            self.lt_list_bullet_rule_file = core_utils.get_os_independent_name(item)
                        case Setup._DCR_CFG_LT_LIST_NUMBER_RULE_FILE:
                            self.lt_list_number_rule_file = core_utils.get_os_independent_name(item)
                        case _:
                            pass

        self._check_config()

        core_glob.logger.debug(core_glob.LOGGER_END)

    # ------------------------------------------------------------------
    # Check the object existence.
    # ------------------------------------------------------------------
    def exists(self) -> bool:
        """Check the object existence.

        Returns:
            bool: Always true.
        """
        return self._exist
