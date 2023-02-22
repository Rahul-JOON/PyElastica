import numpy as np
from numpy.testing import assert_allclose

from elastica._synchronize_periodic_boundary import (
    _synchronize_periodic_boundary_of_matrix_collection,
    _synchronize_periodic_boundary_of_vector_collection,
    _synchronize_periodic_boundary_of_scalar_collection,
)
from elastica.utils import Tolerance
import pytest


@pytest.mark.parametrize("n_elems", [10, 30, 40])
def test_synchronize_periodic_boundary_vector(n_elems):
    """
    Testing the validity of _synchronize_periodic_boundary_of_vector_collection function.

    Parameters
    ----------
    n_elems

    Returns
    -------

    """

    input_vector = np.random.random((3, n_elems + 3))

    periodic_idx = np.zeros((2, 3), dtype=np.int64)
    periodic_idx[0, 0] = 0
    periodic_idx[0, 1] = -2
    periodic_idx[0, 2] = -1

    periodic_idx[1, 0] = -3
    periodic_idx[1, 1] = 1
    periodic_idx[1, 2] = 2

    correct_vector = input_vector.copy()
    correct_vector[..., 0] = input_vector[..., -3]
    correct_vector[..., -2] = input_vector[..., 1]
    correct_vector[..., -1] = input_vector[..., 2]

    _synchronize_periodic_boundary_of_vector_collection(input_vector, periodic_idx)

    assert_allclose(correct_vector, input_vector, atol=Tolerance.atol())


@pytest.mark.parametrize("n_elems", [10, 30, 40])
def test_synchronize_periodic_boundary_matrix(n_elems):
    """
    Testing the validity of _synchronize_periodic_boundary_of_matrix_collection function.

    Parameters
    ----------
    n_elems

    Returns
    -------

    """

    input_matrix = np.random.random((3, 3, n_elems + 3))

    periodic_idx = np.zeros((2, 3), dtype=np.int64)
    periodic_idx[0, 0] = 0
    periodic_idx[0, 1] = -2
    periodic_idx[0, 2] = -1

    periodic_idx[1, 0] = -3
    periodic_idx[1, 1] = 1
    periodic_idx[1, 2] = 2

    correct_matrix = input_matrix.copy()
    correct_matrix[..., 0] = input_matrix[..., -3]
    correct_matrix[..., -2] = input_matrix[..., 1]
    correct_matrix[..., -1] = input_matrix[..., 2]

    _synchronize_periodic_boundary_of_matrix_collection(input_matrix, periodic_idx)

    assert_allclose(correct_matrix, input_matrix, atol=Tolerance.atol())


@pytest.mark.parametrize("n_elems", [10, 30, 40])
def test_synchronize_periodic_boundary_scalar(n_elems):
    """
    Testing the validity of _synchronize_periodic_boundary_of_scalar_collection function.

    Parameters
    ----------
    n_elems

    Returns
    -------

    """

    input_matrix = np.random.random((n_elems + 3))

    periodic_idx = np.zeros((2, 3), dtype=np.int64)
    periodic_idx[0, 0] = 0
    periodic_idx[0, 1] = -2
    periodic_idx[0, 2] = -1

    periodic_idx[1, 0] = -3
    periodic_idx[1, 1] = 1
    periodic_idx[1, 2] = 2

    correct_matrix = input_matrix.copy()
    correct_matrix[..., 0] = input_matrix[..., -3]
    correct_matrix[..., -2] = input_matrix[..., 1]
    correct_matrix[..., -1] = input_matrix[..., 2]

    _synchronize_periodic_boundary_of_scalar_collection(input_matrix, periodic_idx)

    assert_allclose(correct_matrix, input_matrix, atol=Tolerance.atol())


if __name__ == "__main__":
    from pytest import main

    main([__file__])
