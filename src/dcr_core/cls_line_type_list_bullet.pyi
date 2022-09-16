# Copyright (c) 2022 Konnexions GmbH. All rights reserved. Use of this
# source code is governed by the Konnexions Public License (KX-PL)
# Version 2020.05, that can be found in the LICENSE file.

"""Module stub file."""
from __future__ import annotations

import pathlib
import re

import dcr_core.cls_nlp_core as nlp_core

class LineTypeListBullet:
    Entry = dict[str, int | str]
    Entries = list[Entry]
    List = dict[str, Entries | float | int | str]
    Lists = list[List]

    def __init__(
        self,
        file_name_curr: str = "",
    ) -> None:
        self._file_name_curr = ""
        self._environment_variant = ""
        self._anti_patterns: list[tuple[str, re.Pattern[str]]] = []
        self._bullet = ""
        self._entries: list[list[int]] = []
        self._line_idx = 0
        self._line_no_max = 0
        self._lines_json: list[nlp_core.NLPCore.LineJSON] = []
        self._lists: LineTypeListBullet.Lists = []
        self._llx_lower_limit = 0.0
        self._llx_upper_limit = 0.0
        self._no_entries = 0
        self._page_idx = 0
        self._page_idx_prev = 0
        self._para_no_prev = 0
        self._rules: dict[str, int] = {}
        self.no_lists = 0
        self._exist = False
    def _finish_list(self) -> None: ...
    def _init_anti_patterns(self) -> list[tuple[str, re.Pattern[str]]]: ...
    def _init_rules(self) -> dict[str, int]: ...
    @staticmethod
    def _load_anti_patterns_from_json(
        lt_list_bullet_rule_file: pathlib.Path,
    ) -> list[tuple[str, re.Pattern[str]]]: ...
    @staticmethod
    def _load_rules_from_json(
        lt_list_bullet_rule_file: pathlib.Path,
    ) -> dict[str, int]: ...
    def _process_line(self, line_json: nlp_core.NLPCore.LineJSON) -> None: ...
    def _process_page(self) -> None: ...
    def _reset_document(self) -> None: ...
    def _reset_list(self) -> None: ...
    def exists(self) -> bool: ...
    def process_document(
        self,
        directory_name: str,
        document_id: int,
        environment_variant: str,
        file_name_curr: str,
        file_name_orig: str,
    ) -> None: ...
