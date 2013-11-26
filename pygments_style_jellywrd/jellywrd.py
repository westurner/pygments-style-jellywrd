# -*- coding: utf-8 -*-
"""
    Jellywrd Colorscheme
    ~~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class JellywrdStyle(Style):

    background_color = '#040404'
    styles = {
        Comment:            '#888888 bold',
        Comment.Preproc:    '#8fbfdc underline',
        Generic.Deleted:    '#443737 bg:#443737 bold',
        Generic.Emph:       '#80a0ff bold underline',
        Generic.Error:      '#ffffff bg:#a42314 bold',
        Generic.Heading:    '#dd4452 bold',
        Generic.Inserted:   'bg:#454d4d bold',
        Generic.Output:     '#151515 bg:#151515 bold',
        Generic.Subheading: '#dd4452 bold',
        Generic.Traceback:  '#ffffff bg:#ff0000 bold',
        Keyword:            '#8197bf bold',
        Keyword.Type:       '#ffb964 underline',
        Name.Attribute:     '#fad07a',
        Name.Constant:      '#cf6a4c underline',
        Name.Entity:        '#799d6a bold',
        Name.Function:      '#fad07a',
        Name.Tag:           '#8197bf bold',
        Name.Variable:      '#c6b6ee underline',
        String:             '#99ad6a',
        Token:              '#e8e8d3 bg:#040404',
    }
