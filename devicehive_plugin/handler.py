# Copyright (C) 2018 DataArt
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================


class Handler(object):

    def __init__(self, api):
        self._api = api

    @property
    def api(self):
        return self._api

    def disconnect(self):
        self._api.disconnect()

    def handle_connect(self):
        pass

    def handle_event(self, event):
        pass

    def handle_command_insert(self, command):
        pass

    def handle_command_update(self, command):
        pass

    def handle_notification(self, notification):
        pass
