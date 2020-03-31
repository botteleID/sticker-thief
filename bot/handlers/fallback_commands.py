import logging

# noinspection PyPackageRequirements
from telegram.ext import ConversationHandler, CallbackContext
# noinspection PyPackageRequirements
from telegram import Update, ChatAction

from bot.markups import Keyboard
from bot.strings import Strings
from ..utils import decorators

logger = logging.getLogger(__name__)


@decorators.action(ChatAction.TYPING)
@decorators.restricted
@decorators.failwithmessage
@decorators.logconversation
def cancel_command(update: Update, context: CallbackContext):
    logger.info('%s command', update.message.text)

    update.message.reply_text(Strings.CANCEL, reply_markup=Keyboard.HIDE)

    # remove temporary data
    context.user_data.pop('pack', None)
    
    return ConversationHandler.END
