# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""FIFI-LS parameter sets."""

from sofia_redux.pipeline.parameters import Parameters

__all__ = ['FIFILSParameters']


# Store default values for all parameters here.
# They could equivalently be read from a file, or
# constructed programmatically.  All keys are optional;
# defaults are specified in the ParameterSet object.
# All 'key' values should be unique.
DEFAULT = {
    'checkhead': [
        {'key': 'abort',
         'name': 'Abort reduction for invalid headers',
         'value': True,
         'description': 'If set, the reduction will be '
                        'aborted if the input headers '
                        'do not meet requirements',
         'dtype': 'bool',
         'wtype': 'check_box'}
    ],
    'split_grating_and_chop': [
        {'key': 'save',
         'name': 'Save output',
         'value': False,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'parallel',
         'name': 'Use parallel processing',
         'hidden': True,
         'value': False,
         'description': 'If set, processing will be '
                        'distributed across multiple cores.',
         'dtype': 'bool',
         'wtype': 'check_box'},
    ],
    'fit_ramps': [
        {'key': 'save',
         'name': 'Save output',
         'value': False,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'parallel',
         'name': 'Use parallel processing',
         'value': True,
         'hidden': False,
         'description': 'If set, processing will be '
                        'distributed across multiple cores.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 's2n',
         'name': 'Signal-to-noise threshold',
         'value': 10.0,
         'description': 'S/N threshold for data rejection. '
                        'Set to -1 to turn off filtering.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'thresh',
         'name': 'Combination threshold (sigma)',
         'value': 5.0,
         'description': 'Threshold for ramp fit rejection.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'badpix_file',
         'name': 'Bad pixel file',
         'value': '',
         'description': 'Text file containing bad pixel locations',
         'dtype': 'str',
         'wtype': 'pick_file'},
        {'key': 'remove_first',
         'name': 'Remove 1st 2 ramps',
         'value': True,
         'description': 'If set, the first two ramps will '
                        'be removed before fitting.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'subtract_bias',
         'name': 'Subtract bias',
         'value': True,
         'description': 'If set, the value from the open zeroth '
                        'spexel will be subtracted before fitting.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'indpos_sigma',
         'name': 'Threshold for grating instability',
         'value': 3.0,
         'description': 'Threshold in sigma for allowed ramp-averaged '
                        'deviation from expected grating position. \n'
                        'Set to -1 to turn off filtering.',
         'dtype': 'float',
         'wtype': 'text_box'},
    ],
    'subtract_chops': [
        {'key': 'save',
         'name': 'Save output',
         'value': False,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'parallel',
         'name': 'Use parallel processing',
         'value': False,
         'hidden': True,
         'description': 'If set, processing will be '
                        'distributed across multiple cores.',
         'dtype': 'bool',
         'wtype': 'check_box'},
    ],
    'combine_nods': [
        {'key': 'save',
         'name': 'Save output',
         'value': False,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'b_nod_method',
         'name': 'Method for combining off-beam images',
         'wtype': 'combo_box',
         'options': ['nearest', 'average', 'interpolate'],
         'option_index': 0,
         'description': 'For C2NC2 only: nearest takes closest B in time,\n'
                        'average will mean-combine before and after B nods,\n'
                        'interpolate will linearly interpolate before and\n'
                        'after B nods to the A nod time.'},
        {'key': 'offbeam',
         'name': 'Propagate off-beam image instead of on-beam',
         'value': False,
         'description': 'Select to propagate B nods, or to subtract A from B.',
         'dtype': 'bool',
         'wtype': 'check_box'},
    ],
    'lambda_calibrate': [
        {'key': 'save',
         'name': 'Save output',
         'value': False,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'parallel',
         'name': 'Use parallel processing',
         'value': False,
         'hidden': True,
         'description': 'If set, processing will be '
                        'distributed across multiple cores.',
         'dtype': 'bool',
         'wtype': 'check_box'},
    ],
    'spatial_calibrate': [
        {'key': 'save',
         'name': 'Save output',
         'value': False,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'parallel',
         'name': 'Use parallel processing',
         'value': False,
         'hidden': True,
         'description': 'If set, processing will be '
                        'distributed across multiple cores.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'rotate',
         'name': 'Rotate by detector angle',
         'value': True,
         'description': 'If set, output grid is rotated to North up.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'flipsign',
         'name': 'Flip RA/DEC sign convention',
         'wtype': 'radio_button',
         'options': ['flip', 'no flip', 'default'],
         'option_index': 2,
         'description': 'Default will determine correct setting '
                        'from the observation date.'},
    ],
    'apply_static_flat': [
        {'key': 'save',
         'name': 'Save output',
         'value': False,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'parallel',
         'name': 'Use parallel processing',
         'value': False,
         'hidden': True,
         'description': 'If set, processing will be '
                        'distributed across multiple cores.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'skip_flat',
         'name': 'Skip flat correction',
         'value': False,
         'description': 'If set, data will not be flat corrected.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'skip_err',
         'name': 'Skip flat error propagation',
         'value': True,
         'description': 'If set, flat errors will not be propagated.',
         'dtype': 'bool',
         'wtype': 'check_box'},
    ],
    'combine_grating_scans': [
        {'key': 'save',
         'name': 'Save output',
         'value': True,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'parallel',
         'name': 'Use parallel processing',
         'value': False,
         'hidden': True,
         'description': 'If set, processing will be '
                        'distributed across multiple cores.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'bias',
         'name': 'Correct bias offset',
         'value': True,
         'description': 'If set, an additive offset between '
                        'overlapping scans will be removed.',
         'dtype': 'bool',
         'wtype': 'check_box'},
    ],
    'telluric_correct': [
        {'key': 'save',
         'name': 'Save output',
         'value': False,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'parallel',
         'name': 'Use parallel processing',
         'value': False,
         'hidden': True,
         'description': 'If set, processing will be '
                        'distributed across multiple cores.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'skip_tell',
         'name': 'Skip telluric correction',
         'value': False,
         'description': 'If set, data will not be telluric corrected.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'atran_dir',
         'name': 'ATRAN directory',
         'value': '',
         'description': 'Override default set of ATRAN FITS files',
         'dtype': 'str',
         'wtype': 'pick_directory'},
        {'key': 'cutoff',
         'name': 'Cutoff value',
         'value': 0.6,
         'description': 'Below this value in fractional '
                        'transmission, flux values are set to NaN.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'use_wv',
         'name': 'Use WV values',
         'value': False,
         'description': 'If set, water vapor values from the header will '
                        'be used to choose the correct ATRAN file.',
         'dtype': 'bool',
         'wtype': 'check_box'},
    ],
    'flux_calibrate': [
        {'key': 'save',
         'name': 'Save output',
         'value': True,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'parallel',
         'name': 'Use parallel processing',
         'value': False,
         'hidden': True,
         'description': 'If set, processing will be '
                        'distributed across multiple cores.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'skip_cal',
         'name': 'Skip flux calibration',
         'value': False,
         'description': 'If set, data will not be calibrated.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'response_file',
         'name': 'Response file (.fits)',
         'value': '',
         'description': 'Override default response file',
         'dtype': 'str',
         'wtype': 'pick_file'},
    ],
    'correct_wave_shift': [
        {'key': 'save',
         'name': 'Save output',
         'value': False,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'parallel',
         'name': 'Use parallel processing',
         'value': False,
         'hidden': True,
         'description': 'If set, processing will be '
                        'distributed across multiple cores.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'skip_shift',
         'name': 'Skip wavelength shift correction',
         'value': False,
         'description': 'If set, wavelengths will not be corrected.',
         'dtype': 'bool',
         'wtype': 'check_box'},
    ],
    'resample': [
        {'key': 'general_params',
         'name': 'General Parameters',
         'wtype': 'group'},
        {'key': 'save',
         'name': 'Save output',
         'value': True,
         'description': 'Save output data to disk',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'parallel',
         'name': 'Use parallel processing',
         'value': True,
         'hidden': False,
         'description': 'If set, processing will be '
                        'distributed across multiple cores.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'max_cores',
         'name': 'Maximum cores to use',
         'value': '',
         'description': 'Set to the maximum number of cores to use in \n'
                        'parallel processing. If not set, 1/2 of available \n'
                        'cores will be used.',
         'dtype': 'int',
         'wtype': 'text_box'},
        {'key': 'check_memory',
         'name': 'Check memory use during resampling',
         'value': True,
         'description': 'Set to manage memory use and abort if more \n'
                        'memory is needed than is available. \n'
                        'Turn off to attempt processing anyway.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'skip_coadd',
         'name': 'Skip coadd',
         'value': False,
         'description': 'If set, separate cubes will be made '
                        'for each input file.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'interpolate',
         'name': 'Interpolate instead of fit',
         'value': False,
         'description': 'If set, cubes are separately interpolated, '
                        'then mean-combined. Not recommended for '
                        'dithered data.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'error_weighting',
         'name': 'Weight by errors',
         'value': True,
         'description': 'If set, flux fits are inversely weighted '
                        'by the error values.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'fitthresh',
         'name': 'Fit rejection threshold (sigma)',
         'value': -1,
         'description': 'Set higher to keep more fit values.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'posthresh',
         'name': 'Positive outlier threshold (sigma)',
         'value': -1,
         'description': 'Set higher to keep more positive data.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'negthresh',
         'name': 'Negative outlier threshold (sigma)',
         'value': -1,
         'description': 'Set higher to keep more negative data. '
                        'Set to 0 to turn off initial rejection pass.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'append_weights',
         'name': 'Append distance weights to output file',
         'value': False,
         'description': 'If set, distance weights calculated by the '
                        'resampling algorithm will be appended to the '
                        'output FITS file.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'skip_uncorrected',
         'name': 'Skip computing the uncorrected flux cube',
         'value': False,
         'description': 'If set, the uncorrected flux data will be ignored.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'otf_params',
         'name': 'Scan Resampling Parameters',
         'wtype': 'group'},
        {'key': 'scan_reduction',
         'name': 'Use scan reduction before resample',
         'value': False,
         'description': 'If set, a scan reduction will be performed to '
                        'remove additional gains and background before '
                        'resampling.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'save_scan',
         'name': 'Save intermediate scan product',
         'value': False,
         'description': 'If set, the scan product will be saved to '
                        'disk as a FITS file.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'scan_options',
         'name': 'Scan options',
         'value': '',
         'description': 'Parameters to pass to the scan reduction. \n'
                        'Enter as key=value pairs, space-separated.',
         'dtype': 'str',
         'wtype': 'text_box'},
        {'key': 'spatial_params',
         'name': 'Spatial Resampling Parameters',
         'wtype': 'group'},
        {'key': 'detector_coordinates',
         'name': 'Create map in detector coordinates',
         'value': False,
         'description': 'If set, data are combined in arsecond offsets '
                        'from center, rather than sky coordinates. \n'
                        'If not set, detector coordinates are used for '
                        'nonsidereal targets and sky coordinates otherwise.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'xy_oversample',
         'name': 'Spatial oversample (pixels per mean FWHM)',
         'value': 5.0,
         'description': 'Set higher to oversample more.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'xy_pixel_size',
         'name': 'Output spatial pixel size (arcsec)',
         'value': '',
         'description': 'If set, will override oversample parameter.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'xy_order',
         'name': 'Spatial surface fit order',
         'value': 2,
         'description': 'Set lower for more stable fits.',
         'dtype': 'int',
         'wtype': 'text_box'},
        {'key': 'xy_window',
         'name': 'Spatial fit window (factor times FWHM)',
         'value': 3.0,
         'description': 'Set higher to fit more pixels.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'xy_smoothing',
         'name': 'Spatial smoothing radius (factor times FWHM)',
         'value': 1.0,
         'description': 'Set higher to smooth over more pixels.\n'
                        'Set to 0 to turn off distance weights.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'xy_edge_threshold',
         'name': 'Spatial edge threshold (0-1)',
         'value': 0.7,
         'description': 'Set higher to set more edge pixels to NaN.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'adaptive_algorithm',
         'name': 'Adaptive smoothing algorithm',
         'wtype': 'combo_box',
         'options': ['scaled', 'shaped', 'none'],
         'option_index': 2,
         'description': 'If scaled, only the size is allowed to vary.\n'
                        'If shaped, the kernel shape and rotation may \n'
                        'also vary. If none, the kernel will not vary.'},
        {'key': 'spec_params',
         'name': 'Spectral Resampling Parameters',
         'wtype': 'group'},
        {'key': 'w_oversample',
         'name': 'Spectral oversample (pixels per mean FWHM)',
         'value': 8.0,
         'description': 'Set higher to oversample more.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'w_pixel_size',
         'name': 'Output spectral pixel size (um)',
         'value': '',
         'description': 'If set, will override oversample parameter.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'w_order',
         'name': 'Spectral surface fit order',
         'value': 2,
         'description': 'Set lower for more stable fits.',
         'dtype': 'int',
         'wtype': 'text_box'},
        {'key': 'w_window',
         'name': 'Spectral fit window (factor times FWHM)',
         'value': 0.50,
         'description': 'Set higher to fit more pixels.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'w_smoothing',
         'name': 'Spectral smoothing radius (factor times FWHM)',
         'value': 0.25,
         'description': 'Set higher to smooth over more pixels.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'w_edge_threshold',
         'name': 'Spectral edge threshold (0-1)',
         'value': 0.5,
         'description': 'Set higher to set more edge pixels to NaN.',
         'dtype': 'float',
         'wtype': 'text_box'},
    ],
    'specmap': [
        {'key': 'skip_preview',
         'name': 'Skip making the preview image',
         'value': False,
         'description': 'If set, the preview image will not be generated.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'extension',
         'name': 'Extension to map',
         'value': 'FLUX',
         'description': 'Usually FLUX, but UNCORRECTED_FLUX is '
                        'sometimes better.',
         'dtype': 'str',
         'wtype': 'text_box'},
        {'key': 'slice_method',
         'name': 'Method for selecting spectral slice',
         'wtype': 'combo_box',
         'options': ['reference', 'peak'],
         'option_index': 0,
         'description': 'The display image will be selected from the '
                        'cube either at the reference wavelength \n'
                        '(G_WAVE_B/R) or at the peak signal-to-noise '
                        'point in the cube.'},
        {'key': 'point_method',
         'name': 'Method for selecting spatial point',
         'wtype': 'combo_box',
         'options': ['reference', 'peak'],
         'option_index': 1,
         'description': 'The display spectrum will be selected from the '
                        'cube either at the reference position \n'
                        '(OBSLAM/BET) or at the peak flux in the '
                        'selected spectral slice.'},
        {'key': 'override_slice',
         'name': 'Override wavelength slice',
         'value': '',
         'description': 'Manually specify the wavelength slice '
                        '(zero-indexed) for the image.',
         'dtype': 'str',
         'wtype': 'text_box'},
        {'key': 'override_point',
         'name': 'Override spatial point',
         'value': '',
         'description': "Manually specify the spatial "
                        "index for the spectrum, as 'x,y', "
                        "zero-indexed.",
         'dtype': 'str',
         'wtype': 'text_box'},
        {'key': 'ignore_outer',
         'name': 'Fraction of outer wavelengths to ignore',
         'value': 0.2,
         'description': 'Used with method = peak. Set to 0 to include all '
                        'wavelengths in calculating signal peak.',
         'dtype': 'float',
         'wtype': 'text_box'},
        {'key': 'colormap',
         'name': 'Color map',
         'value': 'plasma',
         'description': 'Matplotlib color map name.',
         'dtype': 'str',
         'wtype': 'text_box'},
        {'key': 'scale',
         'name': 'Flux scale for image',
         'value': [0.25, 99.9],
         'description': 'Specify a low and high percentile value for '
                        'the image scale, e.g. [0,99].',
         'dtype': 'floatlist',
         'wtype': 'text_box'},
        {'key': 'n_contour',
         'name': 'Number of contours',
         'value': 0,
         'description': 'Set to 0 to turn off countours.',
         'dtype': 'int',
         'wtype': 'text_box'},
        {'key': 'contour_color',
         'name': 'Contour color',
         'value': 'gray',
         'description': 'Matplotlib color name.',
         'dtype': 'str',
         'wtype': 'text_box'},
        {'key': 'fill_contours',
         'name': 'Filled contours',
         'value': False,
         'description': 'If set, contours will be filled instead of overlaid.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'grid',
         'name': 'Overlay grid',
         'value': False,
         'description': 'If set, a coordinate grid will be overlaid on '
                        'the image.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'beam',
         'name': 'Beam marker',
         'value': False,
         'description': 'If set, a beam marker will be added to the image.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'atran_plot',
         'name': 'Overplot transmission',
         'value': True,
         'description': 'If set, the atmospheric transmission spectrum will\n '
                        'be displayed in the spectral plot.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'error_plot',
         'name': 'Overplot error range',
         'value': True,
         'description': 'If set, the error range will\n '
                        'be overlaid on the spectral plot.',
         'dtype': 'bool',
         'wtype': 'check_box'},
        {'key': 'spec_scale',
         'name': 'Flux scale for spectral plot',
         'value': [0, 100],
         'description': 'Specify a low and high percentile value for '
                        'the spectral flux scale, e.g. [0,99].',
         'dtype': 'floatlist',
         'wtype': 'text_box'},
        {'key': 'watermark',
         'name': 'Watermark text',
         'value': '',
         'description': 'Text to add to image as a watermark.',
         'dtype': 'str',
         'wtype': 'text_box'},
    ],
}


class FIFILSParameters(Parameters):
    """Reduction parameters for the FIFI-LS pipeline."""
    def __init__(self, basehead=None):
        """
        Initialize parameters with default values.

        The baseline header may be used to override default parameters.

        Parameters
        ----------
        basehead : dict-like
            Baseline header for retrieving instrument or observation mode.
        """
        super().__init__(DEFAULT)
        self.basehead = basehead

    def copy(self):
        """
        Return a copy of the parameters.

        Overrides default copy to add in basehead attribute.

        Returns
        -------
        Parameters
        """
        new = super().copy()
        new.basehead = self.basehead.copy()
        return new

    def resample(self, step_index):
        """
        Modify parameters for the resample step.

        Sets default output pixel size by channel.

        Parameters
        ----------
        step_index : int
            Reduction recipe index for the step.
        """
        # read channel from header if possible
        if self.basehead is not None:
            channel = self.basehead.get('DETCHAN', 'UNKNOWN')
            channel = str(channel).strip().upper()
            if channel == 'BLUE':
                self.current[step_index].set_value('xy_pixel_size', 1.5)
            elif channel == 'RED':
                self.current[step_index].set_value('xy_pixel_size', 3.0)
