# Copyright (c) 2022 Konnexions GmbH. All rights reserved. Use of this
# source code is governed by the Konnexions Public License (KX-PL)
# Version 2020.05, that can be found in the LICENSE file.

"""Module stub file."""
from typing import ClassVar

class Setup:
    ENVIRONMENT_TYPE_DEV: ClassVar[str] = ...
    ENVIRONMENT_TYPE_PROD: ClassVar[str] = ...
    ENVIRONMENT_TYPE_TEST: ClassVar[str] = ...

    PDF2IMAGE_TYPE_JPEG: ClassVar[str] = ...
    PDF2IMAGE_TYPE_PNG: ClassVar[str] = ...

    def __init__(self) -> None:
        self.directory_inbox = ""
        self.is_delete_auxiliary_files = False
        self.is_json_incl_config = False
        self.is_json_incl_fonts = False
        self.is_json_incl_heading = False
        self.is_json_incl_list_bullet = False
        self.is_json_incl_list_number = False
        self.is_json_incl_params = False
        self.is_json_sort_keys = False
        self.is_lt_heading_file_incl_regexp = False
        self.is_lt_heading_required = False
        self.is_lt_list_bullet_required = False
        self.is_lt_list_number_file_incl_regexp = False
        self.is_lt_list_number_required = False
        self.is_lt_toc_required = False
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
        self.is_spacy_tkn_attr_cluster = False
        self.is_spacy_tkn_attr_dep_ = False
        self.is_spacy_tkn_attr_doc = False
        self.is_spacy_tkn_attr_ent_iob_ = False
        self.is_spacy_tkn_attr_ent_kb_id_ = False
        self.is_spacy_tkn_attr_ent_type_ = False
        self.is_spacy_tkn_attr_head = False
        self.is_spacy_tkn_attr_i = False
        self.is_spacy_tkn_attr_idx = False
        self.is_spacy_tkn_attr_is_alpha = False
        self.is_spacy_tkn_attr_is_ascii = False
        self.is_spacy_tkn_attr_is_bracket = False
        self.is_spacy_tkn_attr_is_currency = False
        self.is_spacy_tkn_attr_is_digit = False
        self.is_spacy_tkn_attr_is_left_punct = False
        self.is_spacy_tkn_attr_is_lower = False
        self.is_spacy_tkn_attr_is_oov = False
        self.is_spacy_tkn_attr_is_punct = False
        self.is_spacy_tkn_attr_is_quote = False
        self.is_spacy_tkn_attr_is_right_punct = False
        self.is_spacy_tkn_attr_is_sent_end = False
        self.is_spacy_tkn_attr_is_sent_start = False
        self.is_spacy_tkn_attr_is_space = False
        self.is_spacy_tkn_attr_is_stop = False
        self.is_spacy_tkn_attr_is_title = False
        self.is_spacy_tkn_attr_is_upper = False
        self.is_spacy_tkn_attr_lang_ = False
        self.is_spacy_tkn_attr_left_edge = False
        self.is_spacy_tkn_attr_lemma_ = False
        self.is_spacy_tkn_attr_lex = False
        self.is_spacy_tkn_attr_lex_id = False
        self.is_spacy_tkn_attr_like_email = False
        self.is_spacy_tkn_attr_like_num = False
        self.is_spacy_tkn_attr_like_url = False
        self.is_spacy_tkn_attr_lower_ = False
        self.is_spacy_tkn_attr_morph = False
        self.is_spacy_tkn_attr_norm_ = False
        self.is_spacy_tkn_attr_orth_ = False
        self.is_spacy_tkn_attr_pos_ = False
        self.is_spacy_tkn_attr_prefix_ = False
        self.is_spacy_tkn_attr_prob = False
        self.is_spacy_tkn_attr_rank = False
        self.is_spacy_tkn_attr_right_edge = False
        self.is_spacy_tkn_attr_sent = False
        self.is_spacy_tkn_attr_sentiment = False
        self.is_spacy_tkn_attr_shape_ = False
        self.is_spacy_tkn_attr_suffix_ = False
        self.is_spacy_tkn_attr_tag_ = False
        self.is_spacy_tkn_attr_tensor = False
        self.is_spacy_tkn_attr_text = False
        self.is_spacy_tkn_attr_text_with_ws = False
        self.is_spacy_tkn_attr_vocab = False
        self.is_spacy_tkn_attr_whitespace_ = False
        self.is_tokenize_2_jsonfile = False
        self.is_tokenize_2_xmlfile = False
        self.is_verbose = False
        self.is_verbose_lt_header_footer = False
        self.is_verbose_lt_heading = False
        self.is_verbose_lt_list_bullet = False
        self.is_verbose_lt_list_number = False
        self.is_verbose_lt_toc = False
        self.json_indent = 0
        self.lt_footer_max_distance = 0
        self.lt_footer_max_lines = 0
        self.lt_header_max_distance = 0
        self.lt_header_max_lines = 0
        self.lt_heading_file_incl_no_ctx = 0
        self.lt_heading_max_level = 0
        self.lt_heading_min_pages = 0
        self.lt_heading_rule_file = ""
        self.lt_heading_tolerance_llx = 0
        self.lt_list_bullet_min_entries = 0
        self.lt_list_bullet_rule_file = ""
        self.lt_list_bullet_tolerance_llx = 0
        self.lt_list_number_min_entries = 0
        self.lt_list_number_rule_file = ""
        self.lt_list_number_tolerance_llx = 0
        self.lt_toc_last_page = 0
        self.lt_toc_min_entries = 0
        self.pdf2image_type = ""
        self.tesseract_timeout = 0
        self.verbose_parser = ""
    def exists(self) -> bool: ...
