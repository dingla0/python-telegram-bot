#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2022
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
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
"""This module contains the classes that represent Telegram InlineQueryResultCachedGif."""

from typing import TYPE_CHECKING, Any, List, Tuple, Union

from telegram._inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram._inline.inlinequeryresult import InlineQueryResult
from telegram._messageentity import MessageEntity
from telegram._utils.defaultvalue import DEFAULT_NONE
from telegram._utils.types import ODVInput
from telegram.constants import InlineQueryResultType

if TYPE_CHECKING:
    from telegram import InputMessageContent


class InlineQueryResultCachedGif(InlineQueryResult):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this
    animated GIF file will be sent by the user with an optional caption. Alternatively, you can
    use :attr:`input_message_content` to send a message with specified content instead of
    the animation.

    Args:
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        gif_file_id (:obj:`str`): A valid file identifier for the GIF file.
        title (:obj:`str`, optional): Title for the result.caption (:obj:`str`, optional):
        caption (:obj:`str`, optional): Caption of the GIF file to be sent,
            0-:tg-const:`telegram.constants.MessageLimit.CAPTION_LENGTH` characters
            after entities parsing.
        parse_mode (:obj:`str`, optional): Send Markdown or HTML, if you want Telegram apps to show
            bold, italic, fixed-width text or inline URLs in the media caption. See the constants
            in :class:`telegram.constants.ParseMode` for the available modes.
        caption_entities (List[:class:`telegram.MessageEntity`], optional): List of special
            entities that appear in the caption, which can be specified instead of
            :paramref:`parse_mode`.
        reply_markup (:class:`telegram.InlineKeyboardMarkup`, optional): Inline keyboard attached
            to the message.
        input_message_content (:class:`telegram.InputMessageContent`, optional): Content of the
            message to be sent instead of the gif.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        type (:obj:`str`): :tg-const:`telegram.constants.InlineQueryResultType.GIF`.
        id (:obj:`str`): Unique identifier for this result, 1-64 bytes.
        gif_file_id (:obj:`str`): A valid file identifier for the GIF file.
        title (:obj:`str`): Optional. Title for the result.
        caption (:obj:`str`): Optional. Caption of the GIF file to be sent,
            0-:tg-const:`telegram.constants.MessageLimit.CAPTION_LENGTH` characters
            after entities parsing.
        parse_mode (:obj:`str`): Optional. Send Markdown or HTML, if you want Telegram apps to show
            bold, italic, fixed-width text or inline URLs in the media caption. See the constants
            in :class:`telegram.constants.ParseMode` for the available modes.
        caption_entities (List[:class:`telegram.MessageEntity`]): Optional. List of special
            entities that appear in the caption, which can be specified instead of
            :paramref:`parse_mode`.
        reply_markup (:class:`telegram.InlineKeyboardMarkup`): Optional. Inline keyboard attached
            to the message.
        input_message_content (:class:`telegram.InputMessageContent`): Optional. Content of the
            message to be sent instead of the gif.

    """

    __slots__ = (
        'reply_markup',
        'caption_entities',
        'caption',
        'title',
        'input_message_content',
        'parse_mode',
        'gif_file_id',
    )

    def __init__(
        self,
        id: str,  # pylint: disable=redefined-builtin
        gif_file_id: str,
        title: str = None,
        caption: str = None,
        reply_markup: InlineKeyboardMarkup = None,
        input_message_content: 'InputMessageContent' = None,
        parse_mode: ODVInput[str] = DEFAULT_NONE,
        caption_entities: Union[Tuple[MessageEntity, ...], List[MessageEntity]] = None,
        **_kwargs: Any,
    ):
        # Required
        super().__init__(InlineQueryResultType.GIF, id)
        self.gif_file_id = gif_file_id

        # Optionals
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content