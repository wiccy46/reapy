import reapy
from reapy import reascript_api as RPR
from reapy.core import ReapyObject
import typing as ty


class Envelope(ReapyObject):
    id: int
    _parent: ty.Union[ty.Type[reapy.Take], ty.Type[reapy.Track]]

    def __init__(self, parent: ReapyObject, id: int) -> None:
        ...

    @property
    def _args(self) -> ty.Tuple[ReapyObject, int]:
        ...

    def add_item(self, position: float = 0., length: float = 1.,
                 pool: int = 0) -> reapy.AutomationItem:
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
        ...

    def delete_points_in_range(self, start: float, end: float) -> None:
        """
        Delete envelope points between `start` and `end`.

        Parameters
        ----------
        start : float
            Range start in seconds.
        end : float
            Range end in seconds.
        """
        ...

    @reapy.inside_reaper()
    def get_derivatives(self, time: float,
                        raw: bool = False) -> ty.Tuple[float, float, float]:
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
        ...

    @reapy.inside_reaper()
    def get_value(self, time: float,
                  raw: bool = False) -> ty.Union[float, str]:
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
        ...

    @reapy.inside_reaper()
    @property
    def has_valid_id(self) -> bool:
        """
        Whether ReaScript ID is still valid.

        For instance, if envelope has been deleted, ID will not be valid
        anymore.

        :type: bool
        """
        ...

    def insert_envelope_point(self, time: float, value: float = 0.0, shape: int = 0, 
                              tension:float = 0.0, selected: bool = True, no_sort_in: bool = True) -> None:
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
        ...

    def insert_envelope_point_ex(self, autoitem_idx: int, time: float, value: float = 0.0, shape: int = 0, 
                              tension:float = 0.0, selected: bool = True, no_sort_in: bool = True) -> None:
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
        ...

    @property
    def items(self) -> ty.List[reapy.AutomationItem]:
        """
        List of automation items in envelope.

        :type: list of reapy.AutomationItem
        """
        ...

    @property
    def n_items(self) -> int:
        """
        Number of automation items in envelope.

        :type: int
        """
        ...

    @property
    def n_points(self) -> int:
        """
        Number of points in envelope.

        :type: int
        """
        ...

    @property
    def name(self) -> str:
        """
        Envelope name.

        :type: str
        """
        ...

    @property
    def parent(self) -> ty.Union[ty.Type[reapy.Take], ty.Type[reapy.Track]]:
        """
        Envelope parent.

        :type: Take or Track
        """
        ...

    def set_envelope_point(self, ptidx: int, time: Optional[float] = None, value: Optional[float] = None, shape: Optional[int] = None, 
                           tension: Optional[float] = None, selected: Optional[bool] = None, no_sort_in: Optional[bool] = None) -> None:
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
        ...

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
        ...

    def sort_points(self) -> None:
        """Sort all points along the time scale"""
        ...

    def sort_points_ex(self, autoitemidx: int) -> None:
        ...

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
    parent: ty.Union[ty.Type[reapy.Take], ty.Type[reapy.Track]]

    def __init__(self,
                 parent: ty.Union[ty.Type[reapy.Take], ty.Type[reapy.Track]]
                 ) -> None:
        ...

    @property
    def _args(
            self
    ) -> ty.Tuple[ty.Union[ty.Type[reapy.Take], ty.Type[reapy.Track]]]:
        ...

    def __getitem__(self, key: ty.Union[str, int]) -> Envelope:
        ...

    def __len__(self) -> int:
        ...
