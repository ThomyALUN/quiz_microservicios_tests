<?php

namespace App\Http\Controllers;

use App\Models\Genre;

class GenreController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return Genre::with('bands')->get();
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        return Genre::with('bands')->find($id);
    }

}
