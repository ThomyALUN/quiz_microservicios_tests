<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Band;

class BandController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return Band::all();
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        return Band::find($id);
    }

}
