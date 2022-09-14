# Copyright (c) 2022 Konnexions GmbH. All rights reserved. Use of this
# source code is governed by the Konnexions Public License (KX-PL)
# Version 2020.05, that can be found in the LICENSE file.

"""Module stub file."""
import collections
import pathlib
import re

import dcr_core.cls_nlp_core as nlp_core

class LineTypeHeading:
    def __init__(
        self,
        file_name_curr: str = "",
    ) -> None:
        self.file_name_cur = ""
        self._RULE_NAME_SIZE = 0
        self._anti_patterns: list[tuple[str, re.Pattern[str]]] = []
        self._level_prev = None
        self._line_lines_idx = 0
        self._lines_json: list[nlp_core.LineJSON] = []
        self._max_line_line = 0
        self._max_page = 0
        self._page_idx = 0
        self._rules: list[tuple[str, bool, str, collections.abc.Callable[[str, str], bool], list[str]]] = []
        self._rules_collection: list[tuple[str, bool, re.Pattern[str], collections.abc.Callable[[str, str], bool], list[str], str]] = []
        self._rules_hierarchy: list[
            tuple[
                str,
                bool,
                re.Pattern[str],
                collections.abc.Callable[[str, str], bool],
                list[str],
                int,
                str,
                str,
                str,
            ]
        ] = []
        self._toc: list[dict[str, int | object | str]] = []
        self._exist = False
    @staticmethod
    def _check_valid_start_value(target_value: str, is_first_token: bool, start_values: list[str]) -> bool: ...
    def _create_toc_entry(self, level: int, text: str) -> None: ...
    def _get_next_body_line(
        self, page_idx: int, line_lines: list[nlp_core.LineJSON], line_lines_idx: int
    ) -> tuple[str, int, list[nlp_core.LineJSON], int]: ...
    def _init_anti_patterns(self) -> list[tuple[str, re.Pattern[str]]]: ...
    def _init_rules(self) -> list[tuple[str, bool, str, collections.abc.Callable[[str, str], bool], list[str]]]: ...
    @staticmethod
    def _load_anti_patterns_from_json(
        lt_heading_rule_file: pathlib.Path,
    ) -> list[tuple[str, re.Pattern[str]]]: ...
    @staticmethod
    def _load_rules_from_json(
        lt_heading_rule_file: pathlib.Path,
    ) -> list[tuple[str, bool, str, collections.abc.Callable[[str, str], bool], list[str]]]: ...
    def _process_line(self, line_json: nlp_core.LineJSON, text: str, first_token: str) -> int: ...
    def _process_page(self) -> None: ...
    def exists(self) -> bool: ...
    def process_document(
        self,
        directory_name: str,
        document_id: int,
        file_name_curr: str,
        file_name_orig: str,
    ) -> None: ...
