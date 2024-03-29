#!/usr/bin/env python
# pylint: disable=R0903
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains an object that represents a Telegram Bot Command."""
from telegram import TelegramObject


class BotCommand(TelegramObject):
    """
    This object represents a bot command.

    Attributes:
        command (:obj:`str`): Text of the command.
        description (:obj:`str`): Description of the command.

    Args:
        command (:obj:`str`): Text of the command, 1-32 characters. Can contain only lowercase
            English letters, digits and underscores.
        description (:obj:`str`): Description of the command, 3-256 characters.
    """
    def __init__(self, command, description, **kwargs):
        self.command = command
        self.description = description

    @classmethod
    def de_json(cls, data, bot):
        if not data:
            return None

        return cls(**data)
