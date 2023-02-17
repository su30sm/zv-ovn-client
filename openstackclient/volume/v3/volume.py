#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

"""Volume V3 Volume action implementations"""

import logging

from cinderclient import api_versions
from osc_lib.cli import format_columns
from osc_lib.command import command
from osc_lib import exceptions
from osc_lib import utils

from openstackclient.i18n import _


LOG = logging.getLogger(__name__)


class VolumeSummary(command.ShowOne):
    _description = _("Show a summary of all volumes in this deployment.")

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            '--all-projects',
            action='store_true',
            default=False,
            help=_('Include all projects (admin only)'),
        )
        return parser

    def take_action(self, parsed_args):

        volume_client = self.app.client_manager.volume

        if volume_client.api_version < api_versions.APIVersion('3.12'):
            msg = _(
                "--os-volume-api-version 3.12 or greater is required to "
                "support the 'volume summary' command"
            )
            raise exceptions.CommandError(msg)

        columns = [
            'total_count',
            'total_size',
        ]
        column_headers = [
            'Total Count',
            'Total Size',
        ]
        if volume_client.api_version.matches('3.36'):
            columns.append('metadata')
            column_headers.append('Metadata')

        # set value of 'all_tenants' when using project option
        all_projects = parsed_args.all_projects

        vol_summary = volume_client.volumes.summary(
            all_tenants=all_projects,
        )

        return (
            column_headers,
            utils.get_dict_properties(
                vol_summary['volume-summary'],
                columns,
                formatters={'metadata': format_columns.DictColumn},
            ),
        )
