from lib2to3.pgen2.token import OP
import warnings
from typing import Optional

import reapy
from reapy import reascript_api as RPR
from reapy.core import ReapyObject


class Envelope(ReapyObject):

    def __init__(self, parent, id):
        self.id = id
        self._parent = parent

    @property
    def _args(self):
        return (self.parent, self.id)

    def add_item(self, position=0., length=1., pool=0):
        """
        Add automation item to envelope.

        Parameters
        ----------
        position : float, optional
            New item position in seconds (default=0).
        length : float
            New item length in seconds (default=0).
        pool : int
            New item pool index. If >= 0 the automation item will be a
            new instance of that pool (which will be created as an
            empty instance if it does not exist).

        Returns
        -------
        item : reapy.AutomationItem
            New automation item.
        """
        item_index = RPR.InsertAutomationItem(self.id, pool, position, length)
        item = reapy.AutomationItem(envelope=self, index=item_index)
        return item

    def delete_points_in_range(self, start, end):
        """
        Delete envelope points between `start` and `end`.

        Parameters
        ----------
        start : float
            Range start in seconds.
        end : float
            Range end in seconds.
        """
        RPR.DeleteEnvelopePointRange(self.id, start, end)

    @reapy.inside_reaper()
    def get_derivatives(self, time, raw=False):
        """
        Return envelope derivatives of order 1, 2, 3 at a given time.

        Parameters
        ----------
        time : float
            Time in seconds.
        raw : bool, optional
            Whether to return raw values or the human-readable version
            which is printed in REAPER GUI (default=False).

        Returns
        -------
        d, d2, d3 : float
            First, second and third order derivatives.

        Examples
        --------
        >>> envelope = track.envelopes["Pan"]
        >>> envelope.get_derivatives(10, raw=True)
        (0.10635556358181712, 0.2127113398749741, 0.21271155258652666)
        >>> envelope.get_value(10)  # human-readable
        ('10%L', '21%L', '21%L')
        """
        d, d2, d3 = RPR.Envelope_Evaluate(self.id, time, 1, 1, 0, 0, 0, 0)[6:]
        if not raw:
            d = RPR.Envelope_FormatValue(self.id, d, "", 2048)[2]
            d2 = RPR.Envelope_FormatValue(self.id, d2, "", 2048)[2]
            d3 = RPR.Envelope_FormatValue(self.id, d3, "", 2048)[2]
        return d, d2, d3

    @reapy.inside_reaper()
    def get_value(self, time, raw=False):
        """
        Return envelope value at a given time.

        Parameters
        ----------
        time : float
            Time in seconds.
        raw : bool, optional
            Whether to return raw value or its human-readable version,
            which is the one that is printed in REAPER GUI
            (default=False).

        Returns
        -------
        value : float or str
            Envelope value.

        Examples
        --------
        >>> envelope = track.envelopes["Pan"]
        >>> envelope.get_value(10, raw=True)
        -0.5145481809245827
        >>> envelope.get_value(10)  # human-readable
        '51%R'
        """
        value = RPR.Envelope_Evaluate(self.id, time, 0, 0, 0, 0, 0, 0)[5]
        if not raw:
            value = RPR.Envelope_FormatValue(self.id, value, "", 2048)[2]
        return value

    @reapy.inside_reaper()
    @property
    def has_valid_id(self):
        """
        Whether ReaScript ID is still valid.

        For instance, if envelope has been deleted, ID will not be valid
        anymore.

        :type: bool
        """
        try:
            project_id = self.parent.project.id
        except (OSError, AttributeError):
            return False
        pointer, name = self._get_pointer_and_name()
        return bool(RPR.ValidatePtr2(project_id, pointer, name))

    def insert_envelope_point(self, time: float, value: float = 0.0, shape: int = 0, 
                              tension:float = 0.0, selected: bool = True, no_sort_in: bool = True):
        """
        Insert a new automation point.

        Parameters
        ----------
        time : float
            Time in seconds.
        value : float, optional
            Value of the point (0~1.). Default = 0.0
        shape : int, optional
            0 = linear (default), 1 = step, 2 = s-curve, 3 = parabolic opening down, 4 = parabolic opening up,
            5 = parabolic, >5 are just linear. 
        tension : float, optional
            Default = 0.0
        selected : bool, optional
            Default = True
        no_sort_in : bool, optional
            Default = True
        """
        RPR.InsertEnvelopePoint(self.id, time, value, shape, tension, selected, no_sort_in)

    def insert_envelope_point_ex(self, autoitem_idx: int, time: float, value: float = 0.0, shape: int = 0, 
                              tension:float = 0.0, selected: bool = True, no_sort_in: bool = True):
        """
        Note: This method is not fully tested.
        Insert a new automation point, but can be insert into certain automation item. Per envelope can have
        multiple automation items (reapy.AutomationItem), as they can overlap, this method allows targetting 
        on specific item

        Parameters
        ----------
        autoitem_idx: int
            Index of the envelope's automation item, if -1 then use the underlying item
        time : float
            Time in seconds.
        value : float, optional
            Value of the point (0~1.). Default = 0.0
        shape : int, optional
            0 = linear (default), 1 = step, 2 = s-curve, 3 = parabolic opening down, 4 = parabolic opening up,
            5 = parabolic, >5 are just linear. 
        tension : float, optional
            Default = 0.0
        selected : bool, optional
            Default = True
        no_sort_in : bool, optional
            Default = True
        """
        # Todo check if 2nd arg should be self.items[autoitem_idx].id
        RPR.InsertEnvelopePointEx(self.id, autoitem_idx, time, value, shape, tension, selected, no_sort_in)    

    @property
    def items(self):
        """
        List of automation items in envelope.

        :type: list of reapy.AutomationItem
        """
        items = [reapy.AutomationItem(self, i) for i in range(self.n_items)]
        return items

    @property
    def n_items(self):
        """
        Number of automation items in envelope.

        :type: int
        """
        n_items = RPR.CountAutomationItems(self.id)
        return n_items

    @property
    def n_points(self):
        """
        Number of points in envelope.

        :type: int
        """
        n_points = RPR.CountEnvelopePoints(self.id)
        return n_points

    @property
    def name(self):
        """
        Envelope name.

        :type: str
        """
        name = RPR.GetEnvelopeName(self.id, "", 2048)[2]
        return name

    @property
    def parent(self):
        """
        Envelope parent.

        :type: Take or Track
        """
        return self._parent

    def set_envelope_point(self, ptidx: int, time: Optional[float] = None, value: Optional[float] = None, shape: Optional[int] = None, 
                           tension: Optional[float] = None, selected: Optional[bool] = None, no_sort_in: Optional[bool] = None):
        """
        Set attributes of an envelope point.

        Parameters
        ----------
        ptidx: int
            Index of the points in which value is to be set
        time : float
            Time in seconds.
        value : float, optional
            Value of the point (0~1.). Default = 0.0
        shape : int, optional
            0 = linear (default), 1 = step, 2 = s-curve, 3 = parabolic opening down, 4 = parabolic opening up,
            5 = parabolic, >5 are just linear. 
        tension : float, optional
            Default = 0.0
        selected : bool, optional
            Default = True
        no_sort_in : bool, optional
            Default = True
        """
        # TODO check whether None is ok as value
        RPR.SetEnvelopePoint(self.id, ptidx, time, value, shape, tension, selected, no_sort_in)

    def set_envelope_point_ex(self, autoitem_idx: int, ptidx: int, time: Optional[float] = None, 
                              value: Optional[float] = None, shape: Optional[int] = None, 
                              tension: Optional[float] = None, selected: Optional[bool] = None, 
                              no_sort_in: Optional[bool] = None):
        """
        Set attributes of an envelope point onto an AutomationItem

        Parameters
        ----------
        autoitem_idx: int
            Index of the automation item, if == -1, then the target is the underlying envelope
        ptidx: int
            Index of the points in which value is to be set
        time : float
            Time in seconds.
        value : float, optional
            Value of the point (0~1.). Default = 0.0
        shape : int, optional
            0 = linear (default), 1 = step, 2 = s-curve, 3 = parabolic opening down, 4 = parabolic opening up,
            5 = parabolic, >5 are just linear. 
        tension : float, optional
            Default = 0.0
        selected : bool, optional
            Default = True
        no_sort_in : bool, optional
            Default = True
        """
        RPR.SetEnvelopePointEx(self.id, autoitem_idx, ptidx, time, value, shape, tension, selected, no_sort_in)

    def sort_points(self):
        """Sort all points along the time scale"""
        RPR.Envelope_SortPoints(self.id)

    def sort_points_ex(self, autoitemidx: int):
        RPR.Envelope_SortPointsEx(self.id, autoitemidx)


class EnvelopeList(ReapyObject):

    """
    Container class for the list of envelopes on a Take or Track.

    Envelopes can be accessed from the EnvelopeList either by index,
    name or chunk_name (e.g. "<VOLENV").

    Examples
    --------
    >>> len(track.envelopes)
    2
    >>> envelope = track.envelopes[0]
    >>> envelope.name
    'Volume'
    >>> envelope == track.envelopes["Volume"]
    True
    >>> envelope == track.envelopes["<VOLENV"]
    True
    >>> [e.name for e in track.envelopes]
    ['Volume', 'Pan']
    """

    def __init__(self, parent):
        self.parent = parent

    @property
    def _args(self):
        return (self.parent,)

    def __getitem__(self, key):
        parent_type = self.parent.__class__._reapy_parent.__name__
        attr = "Get{}Envelope".format(parent_type)
        if isinstance(key, str):
            if key.startswith("<") and parent_type == 'Track':
                attr += "ByChunkName"
            else:
                attr += "ByName"
        callback = getattr(RPR, attr)
        envelope = Envelope(self.parent, callback(self.parent.id, key))
        if not envelope._is_defined:
            raise KeyError("No envelope for key {}".format(repr(key)))
        return envelope

    def __len__(self):
        return self.parent.n_envelopes
